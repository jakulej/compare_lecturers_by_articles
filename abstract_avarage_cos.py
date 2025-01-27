import json
import os
from dotenv import load_dotenv
import requests
import numpy as np

import db
import author_mapping as am


API_URL = 'https://services.clarin-pl.eu/api/v1/tasks/sent/'
load_dotenv()
API_TOKEN = os.getenv("API_KEY")


HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_TOKEN}'
}

# Funkcja do wysyłania abstraktów do API i uzyskania embeddingów
def get_embeddings(abstracts):
    # Filtrujemy puste lub None wartości
    filtered_abstracts = [abstract for abstract in abstracts if abstract and abstract.strip()]
    
    if not filtered_abstracts:
        print("Brak poprawnych abstraktów do przetworzenia.")
        return []

    data = {
        "application": "similarity",
        "task": "bge-m3",
        "input": filtered_abstracts
    }
    response = requests.post(API_URL, headers=HEADERS, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Błąd {response.status_code}: {response.text}")
        return []

# Funkcja do obliczania średniego embeddingu autora
def calculate_average_embedding(embeddings):
    return np.mean(embeddings, axis=0)

# Funkcja do obliczenia podobieństwa kosinusowego
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# Funkcja do porównania dwóch autorów
def compare_authors(author_id_a, author_id_b):
    # Wyciągnięcie abstraktów
    abstracts_a = [article['description'] for article in db.extract_data(author_id_a) if article['description'] and article['description'].strip()]
    abstracts_b = [article['description'] for article in db.extract_data(author_id_b) if article['description'] and article['description'].strip()]
    
    if not abstracts_a or not abstracts_b:
        return json.dumps({"error": "Brak danych dla jednego z autorów."}, indent=4)
    
    # Uzyskanie embeddingów dla obu autorów
    embeddings_a = get_embeddings(abstracts_a)
    embeddings_b = get_embeddings(abstracts_b)
    
    if not embeddings_a or not embeddings_b:
        return json.dumps({"error": "Błąd przy pobieraniu embeddingów."}, indent=4)
    
    # Obliczanie średnich embeddingów
    mean_embedding_a = calculate_average_embedding(embeddings_a)
    mean_embedding_b = calculate_average_embedding(embeddings_b)
    
    # Obliczanie podobieństwa kosinusowego
    similarity = cosine_similarity(mean_embedding_a, mean_embedding_b)
    
    # Mapowanie ID autorów na imiona i nazwiska
    author_names = am.get_author_names_by_ids([author_id_a, author_id_b])
    
    # Przygotowanie wyniku w formacie JSON
    result = {
        "result": similarity
    }
    
    return json.dumps(result, indent=4)

# Przykładowe wywołanie
# result_json = compare_authors("6602252130", "57204034434")
# print(result_json)

