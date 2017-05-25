import requests

def get(self, steamid, count=10):
    query = "GetRecentlyPlayedGames/v1/?steamid={}&count={}&key={}&format={}"
    query = query.format(steamid, count, self.apikey, self.format)
    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    r = requests.get(self.method + query)
    return r.content
