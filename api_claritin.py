import requests
import numpy as np

# URL API CLARIN-PL
API_URL = 'https://services.clarin-pl.eu/api/v1/tasks/sent/'

# Twój token autoryzacyjny
API_TOKEN = 'SprtBJuLED6J7WBwky07Gj0yhkwEpN7Nl-tP8nd7x6jD7iEc'

# Nagłówki z tokenem
HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_TOKEN}'
}

# Dane wejściowe do analizy podobieństwa
data = {
    "application": "similarity",
    "task": "bge-m3",
    "input": [
        "Tomasz Bombaliński pojechał do Wrocławia.",
        "Jan Nikodem pojechał do Choroszczy."
    ]
}

# Wysyłanie zapytania POST do API
response = requests.post(API_URL, headers=HEADERS, json=data)

# Sprawdzanie odpowiedzi
if response.status_code == 200:
    embeddings = response.json()
    # print("Otrzymane wektory osadzeń:")
    # print(embeddings)

    # Konwersja wektorów na numpy arrays
    vec1 = np.array(embeddings[0])
    vec2 = np.array(embeddings[1])

    # Obliczanie podobieństwa kosinusowego
    cosine_similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    print("\nPodobieństwo kosinusowe:", cosine_similarity)
else:
    print("Błąd:", response.status_code, response.text)
