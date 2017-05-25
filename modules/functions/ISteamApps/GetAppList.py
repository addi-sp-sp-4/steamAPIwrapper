import requests


def get(self):

    query = "GetApplist/v2/?format={}"
    query = query.format(self.format)

    r = requests.get(self.method + query)
    return r.content