import requests


def get(self, appid, classes, language):
    query = "GetAssetclassInfo/v0001/?appid={}&language={}&key={}&format={}"
    query = query.format(appid, language, self.apikey, self.format)

    if type(classes).__name__ != "list":
        print "The 'classes' parameter needs to be a list/array"
        return False

    if not self.apikey:
        print "To use this function an API key is needed"
        return False

    count = len(classes)
    name_string = ""
    for i in range(len(classes)):
        name_string += "&classid{}={}".format(i, classes[i])

    query += "&class_count={}".format(count)
    query += name_string

    r = requests.get(self.method + query)
    return r.content
