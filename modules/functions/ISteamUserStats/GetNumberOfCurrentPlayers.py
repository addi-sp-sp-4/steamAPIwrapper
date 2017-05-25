import requests

def get(self, appid):
    query = "GetNumberOfCurrentPlayers/v1/?appid={}&format={}"
    query = query.format(appid, self.format)

    r = requests.get(self.method + query)
    return r.content