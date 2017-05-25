import functions.ISteamWebAPIUtil.GetServerInfo as GetServerInfo
import functions.ISteamWebAPIUtil.GetSupportedAPIList as GetSupportedAPIList


class ISteamWebAPIUtil():
    def __init__(self, apikey=None, format='json'):
        self.apikey = apikey
        self.format = format
        self.format_possibilities = ['json', 'vdf', 'xml']
        self.url = "http://api.steampowered.com/"
        self.method = self.url + "ISteamWebAPIUtil/"

    def GetServerInfo(self):
        return GetServerInfo.get(self)

    def GetSupportedAPIList(self, key=False):
        return GetSupportedAPIList.get(self, key)



