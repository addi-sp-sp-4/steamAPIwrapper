import functions.IPlayerService.GetRecentlyPlayedGames as GetRecentlyPlayedGames
import functions.IPlayerService.GetOwnedGames as GetOwnedGames
import functions.IPlayerService.GetSteamLevel as GetSteamLevel
import functions.IPlayerService.GetBadges as GetBadges
import functions.IPlayerService.GetCommunityBadgeProgress as GetCommunityBadgeProgress


class IPlayerService():
    def __init__(self, apikey=None, format='json'):

        self.apikey = apikey
        self.format = format
        self.format_possibilities = ['json', 'vdf', 'xml']
        self.url = "http://api.steampowered.com/"
        self.method = self.url + "IPlayerService/"

    def GetRecentlyPlayedGames(self, steamid, count=10):
        return GetRecentlyPlayedGames.get(self, steamid, count)

    def GetOwnedGames(self, steamid, include_appinfo=False, include_played_free_games=False):
        return GetOwnedGames.get(self, steamid, include_appinfo, include_played_free_games)

    def GetSteamLevel(self, steamid):
        return GetSteamLevel.get(self, steamid)

    def GetBadges(self, steamid):
        return GetBadges.get(self, steamid)

    def GetCommunityBadgeProgress(self, steamid, badgeid=False):
        return GetCommunityBadgeProgress.get(self, steamid)

