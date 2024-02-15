import re

class ImageUrlList:
    def __init__(self, str):
        self.find = re.compile("(https://imglf\d.lf127.net/img/.*?(webp|jpg|png|gif|jpeg))")
        self.result = re.findall(self.find, str)
        self.imageurllist = []
        self.number = -1
        self.number2 = -1
        for i in range(0, len(self.result)):
            self.number = self.number + 1
            self.imageurllist.append(self.result[self.number][0])
            self.imageurllist= list(set(self.imageurllist))

imageurllist = ImageUrlList
