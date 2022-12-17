import nltk

# Download necessary resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Function to preprocess text
def preprocess(text):
  # Tokenize the text
  tokens = nltk.word_tokenize(text)

  # Remove stop words
  stop_words = nltk.corpus.stopwords.words('english')
  filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

  # Perform stemming
  stemmer = nltk.stem.PorterStemmer()
  stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

  # Join the tokens back into a single string
  processed_text = ' '.join(stemmed_tokens)

  return processed_text

# Function to extract named entities
def extract_entities(text):
  # Tokenize and tag the text
  tokens = nltk.word_tokenize(text)
  pos_tags = nltk.pos_tag(tokens)

  # Extract named entities
  tree = nltk.ne_chunk(pos_tags)
  named_entities = []
  for subtree in tree.subtrees():
      if subtree.label() == 'NE':
          entity = ' '.join(word for word, pos in subtree.leaves())
          named_entities.append(entity)

  return named_entities

# Read the input text
text = "Barack Obama was born in Honolulu, Hawaii. He served as the 44th President of the United States from 2009 to 2017."

# Preprocess the text
processed_text = preprocess(text)
print("Processed text:", processed_text)

# Extract named entities
named_entities = extract_entities(text)
print("Named entities:", named_entities)
