import functions.ISteamUser.GetFriendList as GetFriendList
import functions.ISteamUser.GetPlayerSummaries as GetPlayerSummaries
import functions.ISteamUser.GetPlayerBans as GetPlayerBans
import functions.ISteamUser.ResolveVanityUrl as ResolveVanityUrl
import functions.ISteamUser.GetUserGroupList as GetUserGroupList


class ISteamUser():
    def __init__(self, apikey=None, format='json'):

        self.apikey = apikey
        self.format = format
        self.format_possibilities = ['json', 'vdf', 'xml']
        self.url = "http://api.steampowered.com/"
        self.method = self.url + "ISteamUser/"

    def GetPlayerSummaries(self, steamids):
        return GetPlayerSummaries.get(self, steamids)

    def GetFriendList(self, steamid, relationship='friend'):
        return GetFriendList.get(self, steamid, relationship)

    def GetPlayerBans(self, steamids):
        return GetPlayerBans.get(self, steamids)

    def ResolveVanityUrl(self, id):
        return ResolveVanityUrl.get(self, id)

    def GetUserGroupList(self, steamid):
        return GetUserGroupList.get(self, steamid)



