import requests


def get(self, key):

    if key:
        if not self.apikey:
            print "To use this function this way an API key is needed"
            return False

        query = "GetSupportedAPIList/v0001/?key={}&format={}"
        query = query.format(self.apikey, self.format)
    else:
        query = "GetSupportedAPIList/v0001/" + "?format=" + self.format

    r = requests.get(self.method + query)
    return r.content

