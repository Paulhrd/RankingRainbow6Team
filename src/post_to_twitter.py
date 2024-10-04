import tweepy
import pandas as pd


class TwitterBot:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def post_ranking(self, rankings: pd.DataFrame):
        message = "Classement Elo des équipes pro de Rainbow Six:\n"
        for idx, row in rankings.iterrows():
            message += f"{idx + 1}. {row['Team']} - Elo: {row['Elo']:.2f}\n"

        self.api.update_status(status=message[:280])  # Limité à 280 caractères sur Twitter
