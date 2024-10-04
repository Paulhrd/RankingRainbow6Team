import pandas as pd


class EloCalculator:
    def __init__(self, K=30, initial_elo=1000):
        self.K = K
        self.initial_elo = initial_elo
        self.elo_ratings = {}

    def initialize_team(self, team_name):
        if team_name not in self.elo_ratings:
            self.elo_ratings[team_name] = self.initial_elo

    def calculate_elo(self, elo1, elo2, result1):
        expected_score1 = 1 / (1 + 10 ** ((elo2 - elo1) / 400))
        new_elo1 = elo1 + self.K * (result1 - expected_score1)
        return new_elo1

    def update_elo(self, team1, team2, result1, result2):
        self.initialize_team(team1)
        self.initialize_team(team2)

        elo1, elo2 = self.elo_ratings[team1], self.elo_ratings[team2]
        new_elo1 = self.calculate_elo(elo1, elo2, result1)
        new_elo2 = self.calculate_elo(elo2, elo1, result2)

        self.elo_ratings[team1] = new_elo1
        self.elo_ratings[team2] = new_elo2

    def get_rankings(self):
        return pd.DataFrame(self.elo_ratings.items(), columns=['Team', 'Elo']).sort_values(by='Elo', ascending=False)
