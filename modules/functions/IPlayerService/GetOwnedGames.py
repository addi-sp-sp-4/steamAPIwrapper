import requests

def get(self, steamid, include_appinfo=False, include_played_free_games=False):
    query = "GetOwnedGames/v1/?steamid={}&include_appinfo={}&include_free_played_games={}&key={}&format={}"
    query = query.format(steamid, include_appinfo, include_played_free_games, self.apikey, self.format)
    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    r = requests.get(self.method + query)
    return r.content