import requests

def get(self, steamid, appid, l='en'):
    query = "GetPlayerAchievements/v1/?steamid={}&appid={}&l={}&format={}&key={}"
    query = query.format(steamid, appid, l, self.format, self.apikey)
    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    r = requests.get(self.method + query)
    return r.content
