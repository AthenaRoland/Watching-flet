import requests
import re

class NameSpider:
    def __init__(self,cookies):
        self.url = "https://www.lofter.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36 ",
            "cookie":f"{cookies}"
        }
        self.spider = requests.post(self.url,headers=self.headers).text
        self.spider = requests.post(url=re.findall('https://.*?\w.lofter.com',re.findall(re.compile('(<a href="https://.*?\w.lofter.com")'),self.spider)[0])[0],headers=self.headers).text
        self.name = re.findall(re.compile('(<a href="/">.*?\w</a>)'),self.spider)[0][12:-4]

namespider = NameSpider