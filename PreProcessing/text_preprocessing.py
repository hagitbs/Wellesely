import spacy
import re
import pandas as pd

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet 
from nltk.stem import PorterStemmer, LancasterStemmer



# Download required resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Load the English pipeline
nlp = spacy.load("en_core_web_sm")

# Initialize stemmers
porter = PorterStemmer()
lancaster = LancasterStemmer() 

filename="/Users/hagitbenshoshan/Documents/Wellesley/Wellesely/PreProcessing/WordFrequencies_data.csv"




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

# Sample usage
text = "Apple Inc. is an American multinational technology company headquartered in Cupertino, California."

results = lemmatize_and_tag_nltk(text)
for lemma, pos in results:
    print(f"Lemmatized: {lemma}, POS: {pos}")

results = stem_and_tag_nltk(text)
for stem, pos in results:
    print(f"stemmed: {stem}, POS: {pos}")

# Read the CSV file
df = pd.read_csv(filename)

result_spacy_csv = []
result_nltk_csv  = []
result_stem_csv  = []

# Process each text in the CSV - spacy
for index, row in df.iterrows():
    text = row['Team 5']
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
        result_spacy_csv.append({"word":lemma,"pos":pos})
    print("\n")
    for lemma, pos in results_nltk:
        print(f"nltk Lemmatized: {lemma}, POS: {pos}")
        result_nltk_csv.append({"word":lemma,"pos":pos})
    print("\n")
    for stem, pos in results_stem:
        print(f"nltk stem: {lemma}, POS: {pos}")
        result_stem_csv.append({"word":stem,"pos":pos})
    print("\n") 

# Convert the result to a DataFrame and save it to a CSV
df = pd.DataFrame(result_spacy_csv)
df.to_csv('result_spacy_csv.csv', index=False)

df = pd.DataFrame(result_nltk_csv)
df.to_csv('result_nltk_csv.csv', index=False)

df = pd.DataFrame(result_stem_csv)
df.to_csv('result_stem_csv.csv', index=False)

 
# Group by 'word' column and count 

result = df.groupby('word').agg({
    'pos': 'max',           # max of 'Value' column
    'word': 'count'    # count of 'OtherColumn'
}).rename(columns={'pos': 'Maxpos', 'word': 'wordCount'})

print(result) 
result.to_csv('agg_result_stem_csv.csv', index=True)
