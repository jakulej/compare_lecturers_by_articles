import json

AUTHOR_PATH = './database/people_PWR.jsonl'

def get_author_name_mapping():
    name_mapping = {}
    with open(AUTHOR_PATH, 'r', encoding='utf-8') as file:
        for line in file:
            person_data = json.loads(line.strip())
            name = f"{person_data['givenname']} {person_data['surname']}"
            eid = person_data['eid'][7:]
            name_mapping[eid] = name
    return name_mapping

def get_author_names_by_ids(author_ids):
    """Funkcja zwraca listę imion i nazwisk dla podanych ID autorów."""
    name_mapping = get_author_name_mapping()
    author_names = []

    for author_id in author_ids:
        name = name_mapping.get(author_id, "Nieznany autor")
        author_names.append(name)

    return author_names

# Przykładowe dane wejściowe
author_ids = ["6602252130", "22136569700", "22135343300", "57220342922"]  # Lista ID autorów

# Pobranie imion i nazwisk autorów
author_names = get_author_names_by_ids(author_ids)

print(author_names)