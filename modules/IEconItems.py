import functions.IEconItems.GetPlayerItems as GetPlayerItems
import functions.IEconItems.GetStoreStatus as GetStoreStatus
import functions.IEconItems.GetStoreMetaData as GetStoreMetadata
import functions.IEconItems.GetSchemaURL as GetSchemaUrl
import functions.IEconItems.GetSchema as GetSchema
import functions.IEconItems.GetEquippedPlayerItems as GetEquippedPlayerItems
import functions.IEconItems.GetPlayerItems_new as GetPlayerItems_new

class IEconItems():
    def __init__(self, apikey=None, format='json'):

        self.apikey = apikey
        self.format = format
        self.format_possibilities = ['json', 'vdf', 'xml']
        self.url = "http://api.steampowered.com/"
        self.method = self.url + "IEconItems_{}/"

    def GetPlayerItems(self, appid, steamid):
        return GetPlayerItems.get(self, appid, steamid)

    def GetStoreStatus(self, appid):
        return GetStoreStatus.get(self, appid)

    def GetStoreMetaData(self, appid, language='en'):
        return GetStoreMetadata.get(self, appid, language)

    def GetSchemaUrl(self, appid):
        return GetSchemaUrl.get(self, appid)

    def GetSchema(self, appid, language='en'):
        return GetSchema.get(self, appid, language)

    def GetEquippedPlayerItems(self, appid, steamid, class_id):
        return GetEquippedPlayerItems.get(self, appid, steamid, class_id)

    def GetPlayerItems_new(self, appid, steamid, l='en', count=5000):
        return GetPlayerItems_new.get(self, appid, steamid, l, count)