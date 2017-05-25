import requests


def get(self):
    query = "GetServerInfo/v0001/?format={}"
    query = query.format(self.format)

    r = requests.get(self.method + query)
    return r.content
