import requests

def fetch_all_scopus_data(api_key, author_id):
    url = f"https://api.elsevier.com/content/search/scopus"
    count = 25  # Liczba rekordów na jedno zapytanie
    start = 0   # Indeks początkowy
    all_entries = []  # Lista na wszystkie rekordy

    while True:
        params = {
            "query": f"AU-ID({author_id})",
            "apiKey": api_key,
            "view": "COMPLETE",
            "start": start
        }

        response = requests.get(url, params=params)

        print(f"Zapytanie od rekordu {start} - Status Code: {response.status_code}")

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break

        try:
            data = response.json()
        except ValueError:
            print("Error: Nie można sparsować odpowiedzi jako JSON.")
            break

        # Pobranie rekordów z bieżącej strony
        entries = data.get("search-results", {}).get("entry", [])
        if not entries:
            print("Brak więcej rekordów do pobrania.")
            break

        for entry in entries:
            parsed_entry = {}
            # Tytuł
            parsed_entry["title"] = entry.get("dc:title")
            # Opis
            parsed_entry["description"] = entry.get("dc:description")
            # Kluczowe słowa (authkeywords)
            authkeywords = entry.get("authkeywords", "")
            parsed_entry["authkeywords"] = [kw.strip() for kw in authkeywords.split('|')] if authkeywords else []
            # Liczba cytowań
            parsed_entry["citedby_count"] = int(entry.get("citedby-count", 0))

            all_entries.append(parsed_entry)

        # Przesuń start do następnego zestawu wyników
        start += count

    return all_entries

# Wprowadzanie danych użytkownika
api_key = "3e9a6d6e6db494dbde4a0c65bf4b9faf"  # Twój klucz API
author_id = "6602252130"

# Pobieranie wszystkich danych
results = fetch_all_scopus_data(api_key, author_id)

# Wyświetlanie wyników
if results:
    print(f"Pobrano {len(results)} rekordów.")
    for idx, entry in enumerate(results, start=1):
        print(f"\n### Publikacja {idx} ###")
        print(f"Tytuł: {entry['title']}")
        print(f"Opis: {entry['description']}")
        print(f"Słowa kluczowe: {', '.join(entry['authkeywords'])}")
        print(f"Liczba cytowań: {entry['citedby_count']}")
