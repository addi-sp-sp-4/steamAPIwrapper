import requests


def get(self, appid, language='en', currency='USD'):
    query = "GetAssetPrices/v0001/?appid={}&language={}&currency={}&key={}&format={}"
    query = query.format(appid, language, currency, self.apikey, self.format)

    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    r = requests.get(self.method + query)
    return r.content
