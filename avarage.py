import matplotlib.pyplot as plt
import numpy as np
import json

FILE_PATH = './database/articles_PWR.jsonl'
PEOPLE_PATH = './database/people_PWR.jsonl'

def extract_data(author_id):
    extracted_data = []
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        for line in file:
            json_data = json.loads(line.strip())
            if author_id not in json_data.get("author_ids", []):
                continue

            data = {
                "pii": json_data.get("pii"),
                "title": json_data.get("title"),
                "subtype": json_data.get("subtype"),
                "author_count": json_data.get("author_count"),
                "author_ids": json_data.get("author_ids"),
                "coverDate": json_data.get("coverDate"),
                "publicationName": json_data.get("publicationName"),
                "description": json_data.get("description"),
                "authkeywords": json_data.get("authkeywords"),
                "fund_sponsor": json_data.get("fund_sponsor"),
                "citedby_count": json_data.get("citedby_count"),
                "interests": json_data.get("author_ids"),  # Assuming interests map to author_ids
                "citedby": json_data.get("citedby_count"),  # Assuming citedby is reflected in citedby_count
            }
            extracted_data.append(data)
    return extracted_data

def get_author_name_mapping():
    name_mapping = {}
    with open(PEOPLE_PATH, 'r', encoding='utf-8') as file:
        for line in file:
            person_data = json.loads(line.strip())
            name = f"{person_data['givenname']} {person_data['surname']}"
            eid = person_data['eid'][7:]
            name_mapping[eid] = name
    return name_mapping

# Przetwarzanie danych dla autorów
author_ids = ["6602252130", "22136569700", "22135343300", "57220342922"]  # Lista ID autorów

name_mapping = get_author_name_mapping()

data_per_author = {}
for author_id in author_ids:
    data = extract_data(author_id)
    citations = [item["citedby_count"] for item in data if item["citedby_count"] is not None]
    keywords = [len(item["authkeywords"] or []) for item in data]
    data_per_author[author_id] = {
        "avg_citations": np.mean(citations) if citations else 0,
        "avg_keywords": np.mean(keywords) if keywords else 0,
    }

# Normalizacja danych
avg_citations = [data["avg_citations"] for data in data_per_author.values()]
avg_keywords = [data["avg_keywords"] for data in data_per_author.values()]

print(avg_citations)
print(avg_keywords)

min_citations, max_citations = 0, max(avg_citations)
min_keywords, max_keywords = 0, max(avg_keywords)

normalized_data = {
    author: {
        "normalized_citations": (data["avg_citations"] - min_citations) / (max_citations - min_citations) if max_citations > min_citations else 0,
        "normalized_keywords": (data["avg_keywords"] - min_keywords) / (max_keywords - min_keywords) if max_keywords > min_keywords else 0,
    }
    for author, data in data_per_author.items()
}

# Przygotowanie danych do wizualizacji
citations_group = [normalized_data[author]["normalized_citations"] for author in normalized_data]
keywords_group = [normalized_data[author]["normalized_keywords"] for author in normalized_data]
authors = [name_mapping.get(author, author) for author in normalized_data]

# Wizualizacja wyników
fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(2)  # Grupy: Cytowania i Słowa kluczowe
width = 0.2  # Szerokość słupków

# Rysowanie słupków dla autorów
for i, author in enumerate(authors):
    ax.bar(x[0] + i * width - width * len(authors) / 2, citations_group[i], width, color=f'C{i}')
    ax.bar(x[1] + i * width - width * len(authors) / 2, keywords_group[i], width, color=f'C{i}')

# Dodanie etykiet i tytułu
ax.set_xlabel("Grupy")
ax.set_ylabel("Znormalizowane wartości")
ax.set_title("Znormalizowane średnie liczby cytowań i słów kluczowych dla autorów")
ax.set_xticks(x)
ax.set_xticklabels(["Cytowania", "Słowa kluczowe"])

# Dodanie legendy
handles = [plt.Rectangle((0, 0), 1, 1, color=f'C{i}') for i in range(len(authors))]
ax.legend(handles, authors, loc="upper right")

plt.ylim(0, 1)
plt.show()
