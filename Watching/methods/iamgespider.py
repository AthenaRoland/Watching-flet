import random
import requests
from .imageurllist import imageurllist


class HomeSpider:
    def __init__(self):
        postnumber = random.randint(0, 55)
        randomnumber = random.randint(0, 1000000)
        self.url = 'https://www.lofter.com/dwr/call/plaincall/PostBean.getHotPosts.dwr'
        self.datas = {
            "callCount": "1",
            "scriptSessionId": "${scriptSessionId}187",
            "httpSessionId": "",
            "c0-scriptName": "PostBean",
            "c0-methodName": "getHotPosts",
            "c0-id": '0',
            "c0-param0": "string:Hot141300",
            "c0-param1": f"number:{postnumber}",
            "batchId": f"{randomnumber}"
        }
        self.headers = {
            "ContentType": "text/plain",
            'Referer': 'https://www.lofter.com/trend?act=qbview_20130930_01',
            "Host": "loftermeirenzhi.lofter.com",
            "Origin": "https://www.lofter.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/79.0.3945.79 Safari/537.36 ",
        }
        self.spider = requests.post(self.url, data=self.datas, headers=self.headers).text
        self.homeimageurl = imageurllist(str=self.spider).imageurllist
        if len(self.homeimageurl) % 2 != 0:
            del self.homeimageurl[-1]


homespider = HomeSpider
