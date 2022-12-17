import nltk

# Download necessary resources
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Tokenize and tag the input sentence
sentence = "Barack Obama was born in Honolulu, Hawaii."
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)

# Extract named entities
tree = nltk.ne_chunk(pos_tags)
named_entities = []
for subtree in tree.subtrees():
    if subtree.label() == 'NE':
        entity = ' '.join(word for word, pos in subtree.leaves())
        named_entities.append(entity)

print(named_entities)
