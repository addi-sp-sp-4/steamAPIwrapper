import requests


def get(self, steamid, badgeid=False):
    query = "GetBadges/v1/?steamid={}&key={}&format={}"

    if badgeid:
        query += "&badgeid={}".format(badgeid)

    query = query.format(steamid, self.apikey, self.format)
    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    r = requests.get(self.method + query)
    return r.content