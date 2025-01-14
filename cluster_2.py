import matplotlib

matplotlib.use('Agg')  # Ustawienie backendu bez GUI
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

import db

result = db.extract_data("6701511885")
result2 = db.extract_data("22136569700")


# Konwersja listy artykułów do DataFrame
def convert_to_dataframe(result, author_label):
    df = pd.DataFrame(result)
    df = df.fillna("")  # Uzupełnienie pustych wartości
    df['author_label'] = author_label  # Dodanie etykiety autora
    return df


# Przetworzenie tekstu (TF-IDF)
def text_to_features(df):
    tfidf = TfidfVectorizer(stop_words="english", max_features=1000)
    text_data = df["title"] + " " + df["description"]
    text_features = tfidf.fit_transform(text_data).toarray()
    return text_features


# Przetworzenie cech liczbowych (standaryzacja)
def numerical_features(df):
    numerical_columns = ["author_count", "citedby_count"]
    numerical_data = df[numerical_columns].values
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(numerical_data)
    return normalized_data


# Połączenie cech tekstowych i liczbowych
def combine_features(text_features, numerical_features):
    return np.hstack((text_features, numerical_features))


# Redukcja wymiarów PCA (do wizualizacji)
def reduce_dimensions(features, n_components=2):
    pca = PCA(n_components=n_components)
    reduced_features = pca.fit_transform(features)
    return reduced_features


# Wizualizacja porównania dwóch autorów
def visualize_comparison(reduced_features, labels, author_labels):
    plt.figure(figsize=(8, 6))
    unique_authors = np.unique(author_labels)

    for author in unique_authors:
        idx = np.where(author_labels == author)
        plt.scatter(reduced_features[idx, 0], reduced_features[idx, 1], label=f'Author {author}', alpha=0.7)

    plt.title('Comparison of Articles by Two Authors')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    plt.savefig("comparison.png")  # Zapisanie wykresu do pliku
    plt.close()


# Przetworzenie danych dla obu autorów
df_result = convert_to_dataframe(result, author_label="Author 1")
df_result2 = convert_to_dataframe(result2, author_label="Author 2")

# Połączenie danych w jedną tabelę
df_combined = pd.concat([df_result, df_result2], ignore_index=True)

# Ekstrakcja cech
text_features_combined = text_to_features(df_combined)
numerical_features_combined = numerical_features(df_combined)
combined_features_combined = combine_features(text_features_combined, numerical_features_combined)

# Redukcja wymiarów do 2D
reduced_features_combined = reduce_dimensions(combined_features_combined, n_components=2)

# Wizualizacja porównania dwóch autorów
visualize_comparison(reduced_features_combined, labels=None, author_labels=df_combined['author_label'].values)
