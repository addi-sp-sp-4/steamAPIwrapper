import functions.ISteamUserStats.GetGlobalAchievementPercentagesForApp as GetGlobalAchievementPercentagesForApp
import functions.ISteamUserStats.GetGlobalStatsForGame as GetGlobalStatsForGame
import functions.ISteamUserStats.GetNumberOfCurrentPlayers as GetNumberOfCurrentPlayers
import functions.ISteamUserStats.GetPlayerAchievements as GetPlayerAchievements
import functions.ISteamUserStats.GetSchemaForGame as GetSchemaForGames
import functions.ISteamUserStats.GetUserStatsForGame as GetUserStatsForGame


class ISteamUserStats():
    def __init__(self, apikey=None, format='json'):

        self.apikey = apikey
        self.format = format
        self.format_possibilities = ['json', 'vdf', 'xml']
        self.url = "http://api.steampowered.com/"
        self.method = self.url + "ISteamUserStats/"

    def GetGlobalAchievementPercentagesForApp(self, gameid):
        return GetGlobalAchievementPercentagesForApp.get(self, gameid)

    def GetGlobalStatsForGame(self, appid, names):
        return GetGlobalStatsForGame.get(self, appid, names)

    def GetNumberOfCurrentPlayers(self, appid):
        return GetNumberOfCurrentPlayers.get(self, appid)

    def GetPlayerAchievements(self, steamid, appid, l='en'):
        return GetPlayerAchievements.get(self, steamid, appid, l)

    def GetSchemaForGames(self, appid, l='en'):
        return GetSchemaForGames.get(self, appid, l)

    def GetUserStatsForGame(self, steamid, appid):
        return GetUserStatsForGame.get(self, steamid, appid)


