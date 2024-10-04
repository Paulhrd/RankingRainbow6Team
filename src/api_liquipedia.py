import requests


class LiquipediaAPI:
    def __init__(self, user_agent):
        self.api_url = "https://liquipedia.net/rainbowsix/api.php"
        self.headers = {
            "User-Agent": user_agent,
            "Accept-Encoding": "gzip"
        }

    def get_match_results(self, page):
        params = {
            "action": "query",
            "format": "json",
            "prop": "revisions",
            "titles": page,
            "rvprop": "content",
            "formatversion": "2"
        }

        response = requests.get(self.api_url, params=params, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Erreur lors de l'appel API : {response.status_code}")
