import requests


def get(self, steamid, relationship):
    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    query = "GetFriendList/v0001/?key={}&steamid={}&relationship={}&format={}"
    query = query.format(self.apikey, steamid, relationship, self.format)
    r = requests.get(self.method + query)
    return r.content

