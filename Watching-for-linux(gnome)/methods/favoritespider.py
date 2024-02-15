import requests
from .imageurllist import imageurllist

class FavoriteSpider:
    def __init__(self, cookies):
        self.url = "https://www.lofter.com/dwr/call/plaincall/PostBean.getFavTrackItem.dwr"
        self.datas = {
            "callCount":"1",
            "scriptSessionId":"${scriptSessionId}187",
            "httpSessionId":"",
            "c0-scriptName":"PostBean",
            "c0-methodName":"getFavTrackItem",
            "c0-id":"0",
            "c0-param0":"number:20",
            "c0-param1":"number:0",
            "batchId":"676571"
        }
        self.headers = {
            "ContentType":"text/plain",
            'Referer': 'https://www.lofter.com/like',
            "Host": "loftermeirenzhi.lofter.com",
            "Origin": "https://www.lofter.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/79.0.3945.79 Safari/537.36 ",
            "cookie":f"{cookies}"
        }
        self.spider = requests.post(self.url, data=self.datas, headers=self.headers).text
        self.favoriteurl = imageurllist(str=self.spider).imageurllist

favoritespider = FavoriteSpider