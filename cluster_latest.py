import matplotlib
matplotlib.use('Agg')  # Ustawienie backendu bez GUI
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import json  # To convert data to JSON format
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import manhattan_distances

import preproces
import author_mapping as am

#do podminay, żeby z fronta brało
# id1 = "6701511885"
# id2 = "56285148000"
# result = preproces.preproces(id1)
# result2 = preproces.preproces(id2)


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
# df_result = convert_to_dataframe(result, author_label=am.get_author_names_by_ids([id1])[0], author_id=id1)
# df_result2 = convert_to_dataframe(result2, author_label=am.get_author_names_by_ids([id2])[0], author_id=id2)

# # Połączenie danych w jedną tabelę
# df_combined = pd.concat([df_result, df_result2], ignore_index=True)

# text_f_1 = text_to_features(df_result)
# text_f_2 = text_to_features(df_result2)

# numerical_f_1 = numerical_features(df_result)
# numerical_f_2 = numerical_features(df_result2)

# combined_f_1 = combine_features(text_f_1, numerical_f_1)
# combined_f_2 = combine_features(text_f_2, numerical_f_2)

# combined_f_data_1 = combined_f_1.tolist()
# combined_f_data_2 = combined_f_2.tolist()
# # Ekstrakcja cech
# text_features_combined = text_to_features(df_combined)
# numerical_features_combined = numerical_features(df_combined)
# combined_features_combined = combine_features(text_features_combined, numerical_features_combined)

# # Przygotowanie danych do wysłania do frontendu
# combined_features_data = combined_features_combined.tolist()  # Lista z danymi połączonymi
# author_labels = df_combined['author_label'].tolist()  # Etykiety autorów
# #author_ids = df_combined['author_id'].tolist()  # Dodanie author_id do danych

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


def compare_all_articles(id1, id2):


    result = preproces.preproces(id1)
    result2 = preproces.preproces(id2)

    df_author1 = convert_to_dataframe(result, author_label=am.get_author_names_by_ids([id1])[0], author_id=id1)
    df_author2 = convert_to_dataframe(result2, author_label=am.get_author_names_by_ids([id2])[0], author_id=id2)
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
    result = {
        "manhattan_similarity": avg_manhattan_similarity,
        "cosine_similarity": avg_cosine_similarity,
        "euclidean_similarity": avg_euclidean_similarity,
    }

    return result


# Zakładając, że df_result i df_result2 są DataFrame zawierającymi dane dla autorów
#avg_manhattan_similarity, avg_cosine_similarity, avg_euclidean_similarity = compare_all_articles(df_result, df_result2)
#print("avg_manhattan_similarity | avg_cosine_similarity | avg_euclidean_similarity")
#print(compare_all_articles(df_result, df_result2))
#print("\n\n")

# # Zwrócenie danych w formacie JSON
# response = {
#     "combinde_f_1": combined_f_data_1,
#     "combinde_f_2": combined_f_data_2,
#     "combined_features": combined_features_data,
#     "author_labels": author_labels,
#     "avg_manhattan_similarity": avg_manhattan_similarity,
#     "avg_cosine_similarity": avg_cosine_similarity,
#     "avg_euclidean_similarity": avg_euclidean_similarity
# }

# print(response)
# # Zamień odpowiedź na JSON
# json_response = json.dumps(response)

# return json_response