from gensim.models import KeyedVectors

# Wczytaj pretrenowany model (np. Google News Word2Vec)
model = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)
print(model.similarity("kid", "baby"))
