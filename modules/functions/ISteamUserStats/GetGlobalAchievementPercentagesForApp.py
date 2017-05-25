import requests


def get(self, gameid):
    query = "GetGlobalAchievementPercentagesForApp/v0002/?gameid={}&format={}"
    query = query.format(gameid, self.format)
    r = requests.get(self.method + query)
    return r.content
