import requests

def get(self, appid, language='en'):
    allowed = ['440', '730', '570', '205790', '620', '841']
    query = "GetSchema/v1/?key={}&language={}format={}"
    query = query.format(self.apikey, language, self.format)
    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    if str(appid) not in allowed:
        print "Unfortunately this method is non-existent for this game"
        return False

    r = requests.get(self.method.format(appid) + query)
    return r.content
