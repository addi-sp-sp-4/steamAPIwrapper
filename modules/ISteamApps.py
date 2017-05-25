import functions.ISteamApps.GetAppList as GetAppList
import functions.ISteamApps.GetServersAtAddress as GetServersAtAddress
import functions.ISteamApps.UpToDateCheck as UpToDateCheck


class ISteamApps():
    def __init__(self, apikey=None, format='json'):

        self.apikey = apikey
        self.format = format
        self.format_possibilities = ['json', 'vdf', 'xml']
        self.url = "http://api.steampowered.com/"
        self.method = self.url + "ISteamApps/"

    def GetAppList(self):
        return GetAppList.get(self)

    def GetServersAtAddress(self, ip4addr):
        return GetServersAtAddress.get(self, ip4addr)

    def UpTodateCheck(self, appid, version):
        return UpToDateCheck.get(self, appid, version)


