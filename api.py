import requests
API_KEY = "7be4c1a4bdecc1dab6074d0ca6606a73"
name = "Jan"
surename = "Nikodem"


request = "https://api.elsevier.com/content/search/scopus?query=AUTHLASTNAME("+ surename +")%20AND%20AUTHFIRST(" + name + ")&apiKey=" + API_KEY
response = requests.get(request)
print(response.json())