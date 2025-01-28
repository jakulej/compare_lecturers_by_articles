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
id1 = "22136569700"
id2 = "22135343300"



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
    similarities = {
        "manhattan": [],
        "cosine": [],
        "euclidean": []
    }
    result = preproces.preproces(id1)
    result2 = preproces.preproces(id2)
    df_author1 = convert_to_dataframe(result, author_label=am.get_author_names_by_ids([id1])[0], author_id=id1)
    df_author2 = convert_to_dataframe(result2, author_label=am.get_author_names_by_ids([id2])[0], author_id=id2)
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
    max_manhatthan_similarity = np.max(similarities["manhattan"])*100
    max_cosine_similarity = np.max(similarities["cosine"]) * 100
    max_euclidean_similarity = np.max(similarities["euclidean"]) * 100
    min_manhatthan_similarity = np.min(similarities["manhattan"])*100
    min_cosine_similarity = np.min(similarities["cosine"]) * 100
    min_euclidean_similarity = np.min(similarities["euclidean"]) * 100

    result = {
            "avg_manhattan_similarity": avg_manhattan_similarity,
            "avg_cosine_similarity": avg_cosine_similarity,
            "avg_euclidean_similarity": avg_euclidean_similarity,
            "max_manhatthan_similarity": max_manhatthan_similarity,
            "max_cosine_similarity": max_cosine_similarity,
            "max_euclidean_similarity": max_euclidean_similarity,
            "min_manhatthan_similarity": min_manhatthan_similarity,
            "min_cosine_similarity": min_cosine_similarity,
            "min_euclidean_similarity": min_euclidean_similarity
    }

    return result


# Zakładając, że df_result i df_result2 są DataFrame zawierającymi dane dla autorów
#print(compare_all_articles(id1, id2))
from sklearn.cluster import DBSCAN

# Funkcja do klasteryzacji za pomocą DBSCAN
def cluster_articles(features, eps=0.5, min_samples=5):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples, metric='euclidean')
    cluster_labels = dbscan.fit_predict(features)
    return cluster_labels

# Dodanie klastrów do danych
def assign_clusters(df, combined_features, eps=0.5, min_samples=5):
    clusters = cluster_articles(combined_features, eps, min_samples)
    df['cluster'] = clusters
    return df

# from sklearn.cluster import KMeans
#
# # Funkcja do klasteryzacji
# def cluster_articles(features, n_clusters=5):
#     kmeans = KMeans(n_clusters=n_clusters, random_state=42)
#     cluster_labels = kmeans.fit_predict(features)
#     return cluster_labels
#
# # Dodanie klastrów do danych
# def assign_clusters(df, combined_features, n_clusters=5):
#     clusters = cluster_articles(combined_features, n_clusters)
#     df['cluster'] = clusters
#     return df


# Modyfikacja funkcji do porównywania artykułów tylko w obrębie tych samych klastrów
def compare_articles_same_cluster(id1, id2):
    similarities = {
        "manhattan": [],
        "cosine": [],
        "euclidean": []
    }
    result = preproces.preproces(id1)
    result2 = preproces.preproces(id2)
    df_author1 = convert_to_dataframe(result, author_label=am.get_author_names_by_ids([id1])[0], author_id=id1)
    df_author2 = convert_to_dataframe(result2, author_label=am.get_author_names_by_ids([id2])[0], author_id=id2)

    text_f_1 = text_to_features(df_author1)
    text_f_2 = text_to_features(df_author2)

    numerical_f_1 = numerical_features(df_author1)
    numerical_f_2 = numerical_features(df_author2)

    combined_f_1 = combine_features(text_f_1, numerical_f_1)
    combined_f_2 = combine_features(text_f_2, numerical_f_2)
    df_result = assign_clusters(df_author1, combined_f_1)
    df_result2 = assign_clusters(df_author2, combined_f_2)
    # Przypisanie klastrów do danych obu autorów
    df_result['cluster'] = cluster_articles(combined_f_1)
    df_result2['cluster'] = cluster_articles(combined_f_2)
    # Iteracja po klastrach
    for cluster_id in set(df_author1['cluster']).intersection(df_author2['cluster']):
        # Wybór artykułów z tego samego klastra
        articles1 = df_author1[df_author1['cluster'] == cluster_id]
        articles2 = df_author2[df_author2['cluster'] == cluster_id]

        for i in range(len(articles1)):
            for j in range(len(articles2)):
                # Wybór cech dla artykułów
                text_features1 = text_to_features(articles1.iloc[i:i + 1])  # cechy tekstowe dla artykułu i
                text_features2 = text_to_features(articles2.iloc[j:j + 1])  # cechy tekstowe dla artykułu j

                # Upewniamy się, że cechy numeryczne są zgodne w wymiarach
                numerical_features1 = numerical_features(articles1.iloc[i:i + 1])  # cechy numeryczne dla artykułu i
                numerical_features2 = numerical_features(articles2.iloc[j:j + 1])  # cechy numeryczne dla artykułu j

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
    max_manhatthan_similarity = np.max(similarities["manhattan"]) * 100
    max_cosine_similarity = np.max(similarities["cosine"]) * 100
    max_euclidean_similarity = np.max(similarities["euclidean"]) * 100
    min_manhatthan_similarity = np.min(similarities["manhattan"]) * 100
    min_cosine_similarity = np.min(similarities["cosine"]) * 100
    min_euclidean_similarity = np.min(similarities["euclidean"]) * 100

    result = {
        "avg_manhattan_similarity": avg_manhattan_similarity,
        "avg_cosine_similarity": avg_cosine_similarity,
        "avg_euclidean_similarity": avg_euclidean_similarity,
        "max_manhatthan_similarity": max_manhatthan_similarity,
        "max_cosine_similarity": max_cosine_similarity,
        "max_euclidean_similarity": max_euclidean_similarity,
        "min_manhatthan_similarity": min_manhatthan_similarity,
        "min_cosine_similarity": min_cosine_similarity,
        "min_euclidean_similarity": min_euclidean_similarity
    }

    return result

#print(compare_articles_same_cluster(id1, id2))