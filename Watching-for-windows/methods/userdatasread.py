import os

class UserDatas():
    with open(r"./datas/userimage.txt", "r") as userimage:
        indexuserimage = userimage.read()
        imagepath = os.path.abspath(r"./datas/userimage.txt")
    with open(r"./datas/fontpath.txt", "r", encoding="utf-8") as userfont:
        indexuserfont = userfont.read()
        fontpath = os.path.abspath(r"./datas/fontpath.txt")
    with open(r"./datas/downloadpath.txt", "r") as userdownloadpath:
        indexuserdownloadpath = userdownloadpath.read()
        downloadpath = os.path.abspath(r"./datas/predownload.txt")
        downloadpath = downloadpath[:-21]
        downloadpath = downloadpath + r"download"
        downloadpathconfig = os.path.abspath(r"./datas/downloadpath.txt")
    with open(r"./datas/fastmode.txt","r") as fastmodeopen:
        iffastmodeopen = fastmodeopen.read()
        fastmodeconfig = os.path.abspath(r"./datas/fastmode.txt")
    with open(r"./datas/cookies.txt","r") as cookies:
        cookiescode = cookies.read()
        cookiesconfig = os.path.abspath(r"./datas/cookies.txt")
    with open(r"./datas/warning.txt","r") as warningmode:
        warningmode = warningmode.read()
        warningconfig = os.path.abspath(r"./datas/warning.txt")

userdatas = UserDatas