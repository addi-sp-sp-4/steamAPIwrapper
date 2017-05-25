import requests

def get(self, id):
    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    query = "ResolveVanityUrl/v0001/?key={}&vanityurl={}&format={}"
    query = query.format(self.apikey, id, self.format)

    r = requests.get(self.method + query)
    return r.content
