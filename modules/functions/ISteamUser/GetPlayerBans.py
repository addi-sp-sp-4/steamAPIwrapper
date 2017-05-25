import requests


def get(self, steamids):
    if type(steamids).__name__ != 'list':
        print "The 'steamids' parameter needs to be an list/array"
        return False

    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    steamids = ','.join(steamids)

    query = "GetPlayerBans/v1/?key={}&steamids={}&format={}"
    query = query.format(self.apikey, steamids, self.format)

    r = requests.get(self.method + query)
    return r.content