from api_liquipedia import LiquipediaAPI
from elo_calculator import EloCalculator
from post_to_twitter import TwitterBot
import pandas as pd
import yaml


def main():
    # Charger la configuration
    with open('config/config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    # Initialiser les composants
    liquipedia_api = LiquipediaAPI(config['liquipedia']['user_agent'])
    elo_calculator = EloCalculator(K=config['elo']['K'], initial_elo=config['elo']['initial_elo'])
    twitter_bot = TwitterBot(config['twitter']['consumer_key'], config['twitter']['consumer_secret'],
                             config['twitter']['access_token'], config['twitter']['access_token_secret'])

    # Récupérer les résultats des matchs depuis Liquipedia
    match_data = liquipedia_api.get_match_results("Six_Major/2023")  # Exemple pour une page de tournoi

    # Calculer les Elo (à partir des résultats, après extraction des données pertinentes)
    elo_calculator.update_elo("Team A", "Team B", 1, 0)
    # Répéter avec les autres matchs...

    # Obtenir les classements actuels
    rankings = elo_calculator.get_rankings()
    print(rankings)

    # Poster sur Twitter
    twitter_bot.post_ranking(rankings)


if __name__ == "__main__":
    main()
