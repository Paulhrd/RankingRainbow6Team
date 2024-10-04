import requests
import json

# URL de l'API MediaWiki pour Liquipedia Rainbow Six
api_url = "https://liquipedia.net/rainbowsix/api.php"

# Paramètres pour l'action 'parse' qui résout les templates
params = {
    "action": "parse",
    "page": "S-Tier_Tournaments",  # Page cible
    "format": "json",
    "prop": "text"
}

# User-Agent personnalisé comme recommandé par Liquipedia
headers = {
    "User-Agent": "EloRankingBot/1.0 (http://www.example.com/; email@example.com)",
    "Accept-Encoding": "gzip"
}

# Faire l'appel API
response = requests.get(api_url, params=params, headers=headers)

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()

    # Extraire et afficher le contenu résolu
    html_content = data.get('parse', {}).get('text', {}).get('*', "")
    print(html_content)
else:
    print(f"Échec de la requête avec le code de statut : {response.status_code}")
