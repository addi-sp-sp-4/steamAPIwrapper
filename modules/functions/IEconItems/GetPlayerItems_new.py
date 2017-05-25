import requests

def get(self, appid, steamid, l='en', count=5000):
    allowed = ['440', '570', '730', '238460', '221540', '205790', '218620', '221540', '620', '841']
    query = "http://steamcommunity.com/inventory/{}/{}/2?l={}&count={}"
    query = query.format(steamid, appid, l, count)

    if str(appid) not in allowed:
        print "Unfortunately this method is non-existent for this game"
        return False

    r = requests.get(query)
    return r.content
