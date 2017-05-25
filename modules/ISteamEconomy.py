import functions.ISteamEconomy.GetAssetClassInfo as GetAssetClassInfo
import functions.ISteamEconomy.GetAssetPrices as GetAssetPrices

class ISteamEconomy():
    def __init__(self, apikey=None, format='json'):

        self.apikey = apikey
        self.format = format
        self.format_possibilities = ['json', 'vdf', 'xml']
        self.url = "http://api.steampowered.com/"
        self.method = self.url + "ISteamEconomy/"

    def GetAssetClassInfo(self, appid, classes, language='en'):
        return GetAssetClassInfo.get(self, appid, classes, language)

    def GetAssetPrices(self, appid, language='en', currency='USD'):
        return GetAssetPrices.get(self, appid, language, currency)
