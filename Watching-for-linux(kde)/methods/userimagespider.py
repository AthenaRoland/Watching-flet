import requests
import re

class UserImageSpider:
    def __init__(self, cookies):
        self.url = "https://www.lofter.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36 ",
            "cookie":f"{cookies}"
        }
        self.spider = requests.post(self.url,headers=self.headers).text
        self.indexurl = re.compile('(<a href="https://.*?\w.lofter.com"><img src="https://.*?(webp|jpg|png)")')
        self.nexturl = re.compile('src="https://.*?\w.net/.*\w[webp|jpg|png|jpeg]"')
        self.finallyurl = re.compile("https://.*?\w.net/.*\w[webp|jpg|png|jpeg]")
        self.indexresult = re.findall(self.indexurl,self.spider)
        self.userimageurl = []
        self.number = -1
        for i in range(0, len(self.indexresult)):
            self.number = self.number + 1
            self.userimageurl.append(self.indexresult[self.number][0])
            self.userimageurl= list(set(self.userimageurl))
        self.nextresult = re.findall(self.nexturl,self.userimageurl[0])
        self.finallyresult = re.findall(self.finallyurl,self.nextresult[0])
        self.finallyresult = self.finallyresult[0]

userimagespider = UserImageSpider