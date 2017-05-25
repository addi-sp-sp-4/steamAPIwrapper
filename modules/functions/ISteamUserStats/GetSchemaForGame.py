import requests

def get(self, appid, l='en'):

    query = "GetSchemaForGame/v2/?appid={}&l={}&key={}&=format={}"
    query = query.format(appid, l, self.apikey, self.format)
    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    r = requests.get(self.method + query)
    return r.content