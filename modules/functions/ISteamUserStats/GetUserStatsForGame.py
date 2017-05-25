import requests

def get(self, steamid, appid):
    query = "GetUserStatsForGame/v2/?steamid={}&appid={}&key={}&format={}"
    query = query.format(steamid, appid, self.apikey, self.format)
    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    r = requests.get(self.method + query)
    return r.content