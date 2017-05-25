import requests


def get(self, ip4addr):
    query = "GetServersAtAddress/v1/?addr={}&format={}"
    query = query.format(ip4addr, self.format)

    r = requests.get(self.method + query)
    return r.content