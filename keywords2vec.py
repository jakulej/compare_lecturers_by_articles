from gensim.models import KeyedVectors

# Wczytanie pretrenowanego modelu Word2Vec
model_path = "GoogleNews-vectors-negative300.bin"  # Ścieżka do pliku z modelem
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# Sprawdzenie wektora dla pojedynczego słowa
vector = model["king"]
print("Wektor dla 'king':", vector)

# Zamiana kilku słów kluczowych na wektor
keywords = ["king", "queen", "royalty"]
combined_vector = sum(model[word] for word in keywords) / len(keywords)
print("Uśredniony wektor dla słów kluczowych:", combined_vector)