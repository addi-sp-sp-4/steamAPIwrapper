import requests

def get(self, appid, steamid):
    allowed = ['440', '570', '730', '238460', '221540', '205790', '218620', '221540', '620', '841']
    query = "GetPlayerItems/v0001/?steamID={}&key={}&format={}"
    query = query.format(steamid, self.apikey, self.format)
    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    if str(appid) not in allowed:
        print "Unfortunately this method is non-existent for this game"
        return False

    r = requests.get(self.method.format(appid) + query)
    return r.content
