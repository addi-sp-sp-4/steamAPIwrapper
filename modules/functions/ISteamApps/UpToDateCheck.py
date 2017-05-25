import requests

def get(self, appid, version):

    query = "UpToDateCheck/v1/?appid={}&version={}&format={}"
    query = query.format(appid, version, self.format)

    r = requests.get(self.method + query)
    return r.content