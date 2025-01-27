import matplotlib.pyplot as plt
import numpy as np
import json

import db
import author_mapping as am


def process_author_data():
    """
    Przetwarza dane autorów, łączy z ich imionami i nazwiskami, normalizuje dane i zwraca w formacie JSON.
    """
    # Lista ID autorów
    author_ids = ["6602252130", "22136569700", "22135343300", "57220342922"]

    # Przetwarzanie danych dla autorów
    data_per_author = {}
    for author_id in author_ids:
        data = db.extract_data(author_id)
        citations = [item["citedby_count"] for item in data if item["citedby_count"] is not None]
        keywords = [len(item["authkeywords"] or []) for item in data]
        data_per_author[author_id] = {
            "avg_citations": np.mean(citations) if citations else 0,
            "avg_keywords": np.mean(keywords) if keywords else 0,
        }

    # Normalizacja danych
    avg_citations = [data["avg_citations"] for data in data_per_author.values()]
    avg_keywords = [data["avg_keywords"] for data in data_per_author.values()]

    min_citations, max_citations = 0, max(avg_citations)
    min_keywords, max_keywords = 0, max(avg_keywords)

    normalized_data = {
        author: {
            "normalized_citations": (data["avg_citations"] - min_citations) / (max_citations - min_citations)
            if max_citations > min_citations else 0,
            "normalized_keywords": (data["avg_keywords"] - min_keywords) / (max_keywords - min_keywords)
            if max_keywords > min_keywords else 0,
        }
        for author, data in data_per_author.items()
    }

    # Pobieranie imion i nazwisk autorów
    author_names = am.get_author_names_by_ids(author_ids)

    # Tworzenie finalnych danych
    final_data = {
        author_id: {
            "name": author_names[i],
            "normalized_citations": normalized_data[author_id]["normalized_citations"],
            "normalized_keywords": normalized_data[author_id]["normalized_keywords"],
        }
        for i, author_id in enumerate(author_ids)
    }

    # Konwersja do formatu JSON
    result_json = json.dumps(final_data, ensure_ascii=False, indent=4)
    return result_json


if __name__ == "__main__":
    result = process_author_data()
    print(result)
