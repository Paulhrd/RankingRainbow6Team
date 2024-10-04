import requests
import json

# URL de l'API MediaWiki pour Liquipedia Rainbow Six
api_url = "https://liquipedia.net/rainbowsix/api.php"

# Paramètres de la requête pour récupérer le contenu d'une page spécifique
params = {
    "action": "query",
    "format": "json",
    "prop": "revisions",
    "titles": "Europe_League/2024/Stage_2",  # Remplace par le nom de la page que tu veux récupérer
    "rvprop": "content",
    "formatversion": "2"
}

# Header User-Agent personnalisé comme demandé par Liquipedia
headers = {
    "User-Agent": "EloRankingBot/1.0 (paul.hrd45@gmail.com)",
    "Accept-Encoding": "gzip"
}

# Faire l'appel à l'API
response = requests.get(api_url, params=params, headers=headers)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Récupérer les données au format JSON
    data = response.json()

    # Afficher le contenu complet reçu
    print(json.dumps(data, indent=4))
else:
    print(f"Échec de la requête avec le code de statut : {response.status_code}")
