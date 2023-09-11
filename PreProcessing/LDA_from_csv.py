import pandas as pd
import gensim
from gensim import corpora
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import spacy
import re

import os

# Read text data from CSV file
# Assume that the CSV file has a column named 'text'
# Get the current working directory
current_path = os.getcwd()
print(current_path)

filename = current_path+'/PreProcessing/WordFrequencies_data_human.csv' 
print (filename) 
df = pd.read_csv(filename)


 

# Pre-processing the texts
def preprocess(document):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(document.lower())
    words_cleaned = [word for word in words if word not in stop_words and word not in string.punctuation]
    return words_cleaned

# Tokenize and clean text

df1=df['Team 1']
df2=df['Team 2']
df3=df['Team 3']
df4=df['Team 4']
df5=df['Team 5']
result_csv=[]
s = pd.concat([df1, df2, df3,df4,df5], ignore_index=True)
df = s.to_frame(name="txt")
for index, row in df.iterrows(): 
    text = row['txt']
    if text is None or pd.isnull(text):
        continue 
    #Clean spcial characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text) 
    if text is None or pd.isnull(text):
        result_csv.append({"text":"NULL","index":index + 1})
    else:
        result_csv.append({"text":text,"index":index + 1}) 

df = pd.DataFrame(result_csv)
print(df)


 
texts = [preprocess(document) for document in df['text']]

# Create a dictionary and corpus
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Apply LDA
NUM_TOPICS = 20
lda_model = gensim.models.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15)

# Print topics and words associated with it
topics = lda_model.print_topics(num_words=5)
for topic in topics:
    print(topic) 