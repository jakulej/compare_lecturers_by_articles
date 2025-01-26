import matplotlib
matplotlib.use('Agg')  # Ustawienie backendu bez GUI
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer #to niepotrzebne
from sklearn.preprocessing import StandardScaler
import json  # To convert data to JSON format

import db
import author_mapping as am

result = db.extract_data("6602252130")
result2 = db.extract_data("22136569700")


# Konwersja listy artykułów do DataFrame
def convert_to_dataframe(result, author_label, author_id):
    df = pd.DataFrame(result)
    df = df.fillna("")  # Uzupełnienie pustych wartości
    df['author_label'] = author_label  # Dodanie etykiety autora
    df['author_id'] = author_id  # Dodanie ID autora
    return df


# zamienić na clarinowe
def text_to_features(df):
    tfidf = TfidfVectorizer(stop_words="english", max_features=1000)
    text_data = df["authkeywords"]
    text_features = tfidf.fit_transform(text_data).toarray()
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


# Przetworzenie danych dla obu autorów, tu z fronta z author_id podmienić
df_result = convert_to_dataframe(result, author_label=am.get_author_names_by_ids(["6602252130"])[0], author_id="6602252130")
df_result2 = convert_to_dataframe(result2, author_label=am.get_author_names_by_ids(["22136569700"])[0], author_id="22136569700")

# Połączenie danych w jedną tabelę
df_combined = pd.concat([df_result, df_result2], ignore_index=True)

# Ekstrakcja cech
text_features_combined = text_to_features(df_combined)
numerical_features_combined = numerical_features(df_combined)
combined_features_combined = combine_features(text_features_combined, numerical_features_combined)

# Przygotowanie danych do wysłania do frontendu
combined_features_data = combined_features_combined.tolist()  # Lista z danymi połączonymi
author_labels = df_combined['author_label'].tolist()  # Etykiety autorów
#author_ids = df_combined['author_id'].tolist()  # Dodanie author_id do danych

# Zwrócenie danych w formacie JSON
response = {
    "combined_features": combined_features_data,
    "author_labels": author_labels,
   # "author_ids": author_ids
}
print(response)
# Zamień odpowiedź na JSON
json_response = json.dumps(response)

# return json_response