import requests

def get(self, steamid):
    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    query = "GetUserGroupList/v1/?key={}&steamid={}&format={}"
    query = query.format(self.apikey, steamid, self.format)

    r = requests.get(self.method + query)
    return r.content