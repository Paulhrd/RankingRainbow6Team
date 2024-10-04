from bs4 import BeautifulSoup

# Parser le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extraire toutes les tables ou div contenant les informations des tournois
tournaments = soup.find_all("table")  # Exemple si les tournois sont dans des tables

for tournament in tournaments:
    print(tournament.text)  # Afficher le contenu de chaque tournoi
