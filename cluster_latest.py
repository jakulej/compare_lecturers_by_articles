import matplotlib
matplotlib.use('Agg')  # Ustawienie backendu bez GUI
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer #to niepotrzebne
from sklearn.preprocessing import StandardScaler
import json  # To convert data to JSON format
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import manhattan_distances
from scipy.spatial.distance import minkowski

import preproces
import author_mapping as am

#do podminay, żeby z fronta brało
id1 = "22135343300"
id2 = "57220342922"
result = preproces.preproces(id1)
result2 = preproces.preproces(id2)


# Konwersja listy artykułów do DataFrame
def convert_to_dataframe(result, author_label, author_id):
    df = pd.DataFrame(result)
    df = df.fillna("")  # Uzupełnienie pustych wartości
    df['author_label'] = author_label  # Dodanie etykiety autora
    df['author_id'] = author_id  # Dodanie ID autora
    return df


def text_to_features(df):
    text_features = np.array(df['authkeywords'].tolist())
    return text_features


# Przetworzenie cech liczbowych (standaryzacja)
def numerical_features(df):
    numerical_columns = ["author_count", "citedby_count", "author_id"]
    numerical_data = df[numerical_columns].values
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(numerical_data)
    return normalized_data


# Połączenie cech tekstowych i liczbowych
def combine_features(text_features, numerical_features):
    return np.hstack((text_features, numerical_features))

# Przetworzenie danych dla obu autorów
df_result = convert_to_dataframe(result, author_label=am.get_author_names_by_ids([id1])[0], author_id=id1)
df_result2 = convert_to_dataframe(result2, author_label=am.get_author_names_by_ids([id2])[0], author_id=id2)

# Połączenie danych w jedną tabelę
df_combined = pd.concat([df_result, df_result2], ignore_index=True)

# Ekstrakcja cech
text_features_combined = text_to_features(df_combined)
numerical_features_combined = numerical_features(df_combined)
#combined_features_combined = combine_features(text_features_combined, numerical_features_combined)
combined_features_combined = numerical_features_combined

# Przygotowanie danych do wysłania do frontendu
combined_features_data = combined_features_combined.tolist()  # Lista z danymi połączonymi
author_labels = df_combined['author_label'].tolist()  # Etykiety autorów
#author_ids = df_combined['author_id'].tolist()  # Dodanie author_id do danych

# Funkcja do obliczania różnych miar podobieństwa
def compute_similarity_metrics(features1, features2):
    # Manhattan distance
    manhattan_dist = manhattan_distances(features1, features2)
    manhattan_similarity = 1 / (1 + manhattan_dist)  # Przekształcenie na podobieństwo

    # Cosine similarity
    cosine_sim = cosine_similarity(features1, features2)

    # Oblicz odległość euklidesową pomiędzy wektorami cech
    euclidean_dist = euclidean_distances(features1, features2)
    # Oblicz podobieństwo jako odwrotność odległości (mniejsze odległości = większe podobieństwo)
    euclidean_sim = 1 / (1 + euclidean_dist)  # Możesz dostosować tę formułę

    return manhattan_similarity[0][0], cosine_sim[0][0], euclidean_sim[0][0]


def compare_all_articles(df_author1, df_author2):
    similarities = {
        "manhattan": [],
        "cosine": [],
        "euclidean": []
    }

    # Iteracja po wszystkich artykułach autora 1 i autora 2
    for i in range(len(df_author1)):
        for j in range(len(df_author2)):
            # Wybór cech dla artykułów autora 1 i 2
            text_features1 = text_to_features(df_author1.iloc[i:i + 1])  # cechy tekstowe dla artykułu i
            text_features2 = text_to_features(df_author2.iloc[j:j + 1])  # cechy tekstowe dla artykułu j

            # Upewniamy się, że cechy numeryczne są zgodne w wymiarach
            numerical_features1 = numerical_features(df_author1.iloc[i:i + 1])  # cechy numeryczne dla artykułu i
            numerical_features2 = numerical_features(df_author2.iloc[j:j + 1])  # cechy numeryczne dla artykułu j

            # Łączenie cech tekstowych i numerycznych w jeden wektor cech
            features1 = np.hstack((text_features1, numerical_features1))
            features2 = np.hstack((text_features2, numerical_features2))

            # Obliczanie podobieństw
            manhattan_sim, cosine_sim, euclidean_sim = compute_similarity_metrics(features1, features2)

            # Dodanie wyników do list
            similarities["manhattan"].append(manhattan_sim)
            similarities["cosine"].append(cosine_sim)
            similarities["euclidean"].append(euclidean_sim)

    # Obliczenie średniego podobieństwa
    avg_manhattan_similarity = np.mean(similarities["manhattan"]) * 100
    avg_cosine_similarity = np.mean(similarities["cosine"]) * 100
    avg_euclidean_similarity = np.mean(similarities["euclidean"]) * 100

    return avg_manhattan_similarity, avg_cosine_similarity, avg_euclidean_similarity


# Zakładając, że df_result i df_result2 są DataFrame zawierającymi dane dla autorów
avg_manhattan_similarity, avg_cosine_similarity, avg_euclidean_similarity = compare_all_articles(df_result, df_result2)
print("avg_manhattan_similarity | avg_cosine_similarity | avg_euclidean_similarity")
print(compare_all_articles(df_result, df_result2))
print("\n\n")


def compare_all_articles_apart(df_author1, df_author2):
    similarities = {
        "manhattan_text": [],
        "manhattan_num": [],
        "cosine_text": [],
        "cosine_num": [],
        "euclidean_text": [],
        "euclidean_num": []
    }

    # Iteracja po wszystkich artykułach autora 1 i autora 2
    for i in range(len(df_author1)):
        for j in range(len(df_author2)):
            # Wybór cech dla artykułów autora 1 i 2
            text_features1 = text_to_features(df_author1.iloc[i:i + 1])  # cechy tekstowe dla artykułu i
            text_features2 = text_to_features(df_author2.iloc[j:j + 1])  # cechy tekstowe dla artykułu j

            # Upewniamy się, że cechy numeryczne są zgodne w wymiarach
            numerical_features1 = numerical_features(df_author1.iloc[i:i + 1])  # cechy numeryczne dla artykułu i
            numerical_features2 = numerical_features(df_author2.iloc[j:j + 1])  # cechy numeryczne dla artykułu j

            # Obliczanie podobieństw
            manhattan_text_sim, cosine_text_sim, euclidean_text_sim = compute_similarity_metrics(text_features1, text_features2)
            manhattan_num_sim, cosine_num_sim, euclidean_num_sim= compute_similarity_metrics(numerical_features1, numerical_features2)

            # Dodanie wyników do list
            similarities["manhattan_text"].append(manhattan_text_sim)
            similarities["manhattan_num"].append(manhattan_num_sim)
            similarities["cosine_text"].append(cosine_text_sim)
            similarities["cosine_num"].append(cosine_num_sim)
            similarities["euclidean_text"].append(euclidean_text_sim)
            similarities["euclidean_num"].append(euclidean_num_sim)

    # Obliczenie średniego podobieństwa
    avg_manhattan_text_similarity = np.mean(similarities["manhattan_text"]) * 100
    avg_manhattan_num_similarity = np.mean(similarities["manhattan_num"]) * 100
    avg_cosine_text_similarity = np.mean(similarities["cosine_text"]) * 100
    avg_cosine_num_similarity = np.mean(similarities["cosine_num"]) * 100
    avg_euclidean_text_similarity = np.mean(similarities["euclidean_text"]) * 100
    avg_euclidean_num_similarity = np.mean(similarities["euclidean_num"]) * 100

    return {
        "avg_manhattan_text_similarity_percentage": avg_manhattan_text_similarity,
        "avg_manhattan_num_similarity_percentage": avg_manhattan_num_similarity,
        "avg_cosine_text_similarity_percentage": avg_cosine_text_similarity,
        "avg_cosine_num_similarity_percentage": avg_cosine_num_similarity,
        "avg_euclidean_text_similarity_percentage": avg_euclidean_text_similarity,
        "avg_euclidean_num_similarity_percentage": avg_euclidean_num_similarity,
    }

print("apart:\n")
print(compare_all_articles_apart(df_result, df_result2))
print("\n\n")
# Funkcja do obliczania podobieństwa na podstawie odległości euklidesowej
def compute_similarity_euklides(features1, features2):
    # Oblicz odległość euklidesową pomiędzy wektorami cech
    distance = euclidean_distances(features1, features2)
    # Oblicz podobieństwo jako odwrotność odległości (mniejsze odległości = większe podobieństwo)
    similarity = 1 / (1 + distance)  # Możesz dostosować tę formułę
    return similarity[0][0]  # Zwraca wartość podobieństwa jako pojedynczy element

# Zwrócenie danych w formacie JSON
response = {
    "combined_features": combined_features_data,
    "author_labels": author_labels,
   # "author_ids": author_ids
}
#print(response)
# Zamień odpowiedź na JSON
json_response = json.dumps(response)

# return json_response