import matplotlib

matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import db

result = db.extract_data("6701511885")

# Convert result data to a DataFrame
def convert_to_dataframe(result):
    df = pd.DataFrame(result)
    # Handle missing values
    df = df.fillna("")
    return df


# Convert titles and descriptions into TF-IDF vectors
def text_to_features(df):
    tfidf = TfidfVectorizer(stop_words="english", max_features=1000)
    text_data = df["title"] + " " + df["description"]  # Combine title and description for clustering
    text_features = tfidf.fit_transform(text_data).toarray()
    return text_features


# Standardize numerical features
def numerical_features(df):
    numerical_columns = ["author_count", "citedby_count"]
    numerical_data = df[numerical_columns].values
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(numerical_data)
    return normalized_data


# Combine textual and numerical features
def combine_features(text_features, numerical_features):
    return np.hstack((text_features, numerical_features))


# Apply KMeans clustering
def apply_kmeans(features, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(features)
    return kmeans


# Visualize clusters
def visualize_clusters(features, kmeans):
    plt.scatter(features[:, 0], features[:, 1], c=kmeans.labels_, cmap='viridis')
    plt.title('KMeans Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.savefig("clusters.png")  # Save the plot as a PNG file
    plt.close()  # Close the plot to free up memory

from sklearn.decomposition import PCA

# Redukcja wymiarów za pomocą PCA
def reduce_dimensions(features, n_components=2):
    pca = PCA(n_components=n_components)
    reduced_features = pca.fit_transform(features)
    return reduced_features

# Wizualizacja z wykorzystaniem PCA
def visualize_clusters_pca(features, kmeans):
    reduced_features = reduce_dimensions(features, n_components=2)  # Redukcja do 2 wymiarów
    plt.scatter(reduced_features[:, 0], reduced_features[:, 1], c=kmeans.labels_, cmap='viridis')
    plt.title('KMeans Clustering')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.savefig("clusters.png")  # Zapisanie wykresu jako PNG
    plt.close()  # Zamknięcie wykresu po zapisaniu


# Process the data
df_result = convert_to_dataframe(result)

# Extract features
text_features_result = text_to_features(df_result)
numerical_features_result = numerical_features(df_result)
combined_features_result = combine_features(text_features_result, numerical_features_result)

# Apply clustering
kmeans_result = apply_kmeans(combined_features_result, n_clusters=3)

# Visualize clustering and save to a file
visualize_clusters_pca(combined_features_result, kmeans_result)
