import json
from .userdataschange import UserDatasChange

class Defaultconfig():
    with open(r"./datas/default.json", "r+", encoding="utf-8") as file:
        data = json.loads(file.read())
        defaultimagepath = data[0]["defaultimagepath"]
        defaultrdownloadpath = data[0]["defaultrdownloadpath"]
        defaultfontpath = data[0]["defaultfontpath"]
        defaultfastmodconfig = data[0]["defaultfastmodeconfig"]
    
