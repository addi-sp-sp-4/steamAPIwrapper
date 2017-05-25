import requests

def get(self, appid):
    allowed = ['440']
    query = "GetStoreStatus/v1/?key={}&format={}"
    query = query.format(self.apikey, self.format)
    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    if str(appid) not in allowed:
        print "Unfortunately this method is non-existent for this game"
        return False

    r = requests.get(self.method.format(appid) + query)
    return r.content
