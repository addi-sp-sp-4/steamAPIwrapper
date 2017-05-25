import requests


def get(self, appid, count, maxlength):
    query = "GetNewsForApp/v0002/?appid={}&count={}&maxlength={}&format={}"
    query = query.format(appid, str(count), str(maxlength), self.format)

    r = requests.get(self.method + query)
    return r.content
