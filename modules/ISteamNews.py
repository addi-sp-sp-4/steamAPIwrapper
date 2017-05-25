import functions.ISteamNews.GetNewsForApp as GetNewsForApp


class ISteamNews():
    def __init__(self, apikey=None, format='json'):

        self.apikey = apikey
        self.format = format
        self.format_possibilities = ['json', 'vdf', 'xml']
        self.url = "http://api.steampowered.com/"
        self.method = self.url + "ISteamNews/"

    def GetNewsForApp(self, appid, count=3, maxlength=300):
        return GetNewsForApp.get(self, appid, count, maxlength)





