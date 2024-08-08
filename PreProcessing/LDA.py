import gensim
from gensim import corpora
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import nltk
nltk.download('stopwords')

# Sample texts
documents = [
    "Natural language processing is a subfield of artificial intelligence.",
    "Artificial intelligence is creating a revolution in the tech industry.",
    "Machine learning is an approach to achieve artificial intelligence.",
    "Deep learning algorithms require large datasets and significant amounts of compute power.", 
    "Alice just woked up in the morning in wonderland with fairies",
    "bag that uses bag bag bag sensor to alert you if something you took out wasn't placed back in after its been closed to prevent loss"

]

# Pre-processing the texts
def preprocess(document):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(document.lower())
    words_cleaned = [word for word in words if word not in stop_words and word not in string.punctuation]
    print(words_cleaned)
    return words_cleaned

texts = [preprocess(document) for document in documents]

# Create a dictionary and corpus
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Apply LDA
# The passes parameter controls how often we train the model on the entire corpus
NUM_TOPICS = 6
lda_model = gensim.models.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15)

# Print topics and words associated with it
topics = lda_model.print_topics(num_words=5)
for topic in topics:
    print(topic)

# Note: Ensure you've installed the necessary libraries like nltk and gensim before running this script.
