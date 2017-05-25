import requests


def get(self, appid, names):
    query = "GetGlobalStatsForGame/v0001/?appid={}&format={}"
    query = query.format(appid, self.format)

    if type(names).__name__ != "list":
        print "The 'names' parameter needs to be a list/array"
        return False
    count = len(names)
    name_string = ""
    for i in range(len(names)):
        name_string += "&name[{}]={}".format(i, names[i])

    query += "&count={}".format(count)
    query += name_string
    r = requests.get(self.method + query)
    return r.content
