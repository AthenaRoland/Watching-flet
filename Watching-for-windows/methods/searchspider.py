import requests
from urllib.parse import quote
import random
from .imageurllist import imageurllist

class SearchList:
    def __init__(self,searchvalue,offset):
        self.number = "1707972"
        self.randomnumber = str(random.randint(1,1000000))
        self.url = f"https://www.lofter.com/newsearch/post.json?key={quote(searchvalue)}&limit=10&offset={offset}&_={self.number}{self.randomnumber}"
        self.headers = {
            "key":f"{quote(searchvalue)}",
            "limit":"10",
            "offset":f"{offset}",
            "_":f"{self.number}{self.randomnumber}",
            "Referer":f"https://www.lofter.com/front/homesite/search?type=post&q={quote(searchvalue)}",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/79.0.3945.79 Safari/537.36 ",
            "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"
        }
        self.spider = imageurllist(str=requests.get(self.url,headers=self.headers).text).imageurllist

searchlist = SearchList