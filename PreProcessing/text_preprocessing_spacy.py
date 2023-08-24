import spacy
import re
import pandas as pd

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet 
from nltk.stem import PorterStemmer, LancasterStemmer
import os




# Download required resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Load the English pipeline
nlp = spacy.load("en_core_web_sm")

# Initialize stemmers
porter = PorterStemmer()
lancaster = LancasterStemmer() 

# Get the current working directory
current_path = os.getcwd()
print(current_path)

filename = current_path+'/PreProcessing/WordFrequencies_data.csv' 
print (filename) 
df = pd.read_csv(filename)




def tokenize(text):
    """Tokenize the given text."""
    doc = nlp(text)
    return [token.text for token in doc]

def lemmatize(text):
    """Lemmatize the given text."""
    doc = nlp(text)
    return [token.lemma_ for token in doc]

def classify(text):
    """Classify named entities in the given text."""
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def lemmatize_and_tag(text):
    """Lemmatize the given text and tag if it's a noun or adjective."""
    doc = nlp(text)
    return [(token.lemma_, token.pos_) for token in doc if token.pos_ in ['NOUN', 'ADJ','VERB']] 



# Sample usage
text = "Apple Inc. is an American multinational technology company headquarter locates in Cupertino, California."

print("Tokens:", tokenize(text))
print("Lemmas:", lemmatize(text))
print("Entities:", classify(text))
results = lemmatize_and_tag(text)
for lemma, pos in results:
    print(f"Lemmatized: {lemma}, POS: {pos}")

# Same code with NLTK 

def get_wordnet_pos(treebank_tag):
    """Map treebank POS tag to first character used by WordNetLemmatizer."""
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default to noun

def lemmatize_and_tag_nltk(text):
    """Lemmatize the given text and tag if it's a noun or adjective using nltk."""
    tokens = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    
    lemmatizer = WordNetLemmatizer()

    return [(lemmatizer.lemmatize(token, get_wordnet_pos(pos)), pos) for token, pos in pos_tags    if pos in ['NN','NNS', 'JJ'] or pos.startswith("V") ]


# Stemming with Porter Stemmer
def stem_and_tag_nltk(text):
    tokens = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)

    return  [(porter.stem(token, get_wordnet_pos(pos)), pos) for token, pos in pos_tags    if pos in ['NN','NNS', 'JJ'] or pos.startswith("V") ] 

# Stemming with Lancaster Stemmer
# lancaster_stems = [lancaster.stem(word) for word in words] 
 
# Read the CSV file
df = pd.read_csv(filename)

result_spacy_csv = []
result_nltk_csv  = []
result_stem_csv  = []

df1=df['Team 1']
df2=df['Team 2']
df3=df['Team 3']
df4=df['Team 4']
df5=df['Team 5']

s = pd.concat([df1, df2, df3,df4,df5], ignore_index=True)
df = s.to_frame(name="txt")

print ( df ) 
# Process each text in the CSV - spacy
for index, row in df.iterrows(): 
    text = row['txt']
    if text is None or pd.isnull(text):
        continue 
    #Clean spcial characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    results = lemmatize_and_tag(text)
    results_nltk=lemmatize_and_tag_nltk(text)
    results_stem=stem_and_tag_nltk(text)

    print(f"Text {index + 1}:")
    for lemma, pos in results:
        print(f"Spacy Lemmatized: {lemma}, POS: {pos}")
        result_spacy_csv.append({"word":lemma,"pos":pos,"vector":index + 1})
    print("\n")
    for lemma, pos in results_nltk:
        print(f"nltk Lemmatized: {lemma}, POS: {pos}")
        result_nltk_csv.append({"word":lemma,"pos":pos,"vector":index + 1}) 
    print("\n")
    for stem, pos in results_stem:
        print(f"nltk stem: {lemma}, POS: {pos}")
        result_stem_csv.append({"word":stem,"pos":pos,"vector":index + 1}) 
    print("\n") 

# Convert the result to a DataFrame and save it to a CSV
df = pd.DataFrame(result_spacy_csv)
df.to_csv('result_spacy_csv.csv', index=False)

 

 
# Group by 'word' column and count (DVR)

result = df.groupby('word').agg({
    'pos': 'max',           # max of 'Value' column
    'word': 'count'    # count of 'OtherColumn'
}).rename(columns={'pos': 'Maxpos', 'word': 'wordCount'})

dfglobal=result
print(result) 
result.to_csv('agg_result_stem_csv.csv', index=True)


# Generate vectors per author 
result = df.groupby(['vector', 'word']).agg({
    'pos': 'max',           # max of 'Value' column
    'word': 'count'    # count of 'OtherColumn'
}).rename(columns={'pos': 'Maxpos', 'word': 'wordCount'})
dflocal=result

print(dflocal) 
dflocal.to_csv('agg_vector_stem_csv.csv', index=True)

# Calculate Frequencies and distances 

# Calculate the total sum
total_sum = dfglobal['wordCount'].sum()

# Calculate the percentage of the total for each value (Global)
dfglobal['percent_of_total'] = (dfglobal['wordCount'] / total_sum) * 100

dfglobal = dfglobal.sort_values('percent_of_total', ascending=False)

print(dfglobal)

# Calculate the percentage of the total for each value (local)
 
total_sum_by_category = dflocal.groupby('vector')['wordCount'].transform('sum')

# Calculate the percent of total within each category
dflocal['percent_of_total'] = (dflocal['wordCount'] / total_sum_by_category) * 100

# Optionally, sort the DataFrame by 'category' and 'percent_of_total'
dflocal = dflocal.sort_values(['vector', 'percent_of_total'], ascending=[True, False])

print(dflocal)

 
# Merge dflocal and dfglobal to the same CSV file  
 
merged_df = pd.merge(dflocal, dfglobal, on='word',   how='outer')

print(merged_df) 