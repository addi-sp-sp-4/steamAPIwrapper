from modules.ISteamUser import ISteamUser as ISteamUser
from modules.ISteamUserStats import ISteamUserStats as ISteamUserStats
from modules.ISteamNews import ISteamNews as ISteamNews
from modules.ISteamWebAPIUtil import ISteamWebAPIUtil as ISteamWebAPIUtil
from modules.ISteamApps import ISteamApps as ISteamApps
from modules.ISteamEconomy import ISteamEconomy as ISteamEconomy
from modules.IPlayerService import IPlayerService as IPlayerService
from modules.IEconItems import IEconItems as IEconItems

class Wrapper:
    def __init__(self, apikey=None, format='json'):

        self.ISteamUser = ISteamUser(apikey, format)
        self.ISteamUserStats = ISteamUserStats(apikey, format)
        self.ISteamNews = ISteamNews(apikey, format)
        self.ISteamWebAPIUtil = ISteamWebAPIUtil(apikey, format)
        self.ISteamApps = ISteamApps(apikey, format)
        self.ISteamEconomy = ISteamEconomy(apikey, format)
        self.IPlayerService = IPlayerService(apikey, format)
        self.IEconItems = IEconItems(apikey, format)
        self.format = format
        self.apikey = apikey
        self.format_possibilities = ['xml', 'vdf', 'json']

        if self.format not in self.format_possibilities:
            print "Warning, the 'format' parameter may be invalid"

