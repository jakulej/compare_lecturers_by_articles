

def get_vec(keywords):
    from dotenv import load_dotenv
    import os
    import requests
    import numpy as np

    # URL API CLARIN-PL
    API_URL = 'https://services.clarin-pl.eu/api/v1/tasks/sent/'

    # Twój token autoryzacyjny
    load_dotenv()
    API_TOKEN = os.getenv("API_KEY")
    # Nagłówki z tokenem
    HEADERS = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_TOKEN}'
    }

    # Dane wejściowe do analizy podobieństwa
    data = {
        "application": "similarity",
        "task": "bge-m3",
        "input": [keywords]
    }

    # Wysyłanie zapytania POST do API
    response = requests.post(API_URL, headers=HEADERS, json=data)

    # Sprawdzanie odpowiedzi
    if response.status_code == 200:
        embeddings = response.json()[0]
        return(embeddings)
    else:
        return(response.status_code)
get_vec("boiling curves | heat transfer coefficient | low-pressure refrigerant | Nucleate boiling")
