import flet as ft
import subprocess
import random
import requests
from views.index_gridview import ImageView
from views.views_spread import *
from methods.userdatasread import userdatas
from methods.imageurllist import imageurllist
from methods.userdataschange import UserDatasChange
from methods.default import Defaultconfig
from methods.iamgespider import homespider
from methods.favoritespider import favoritespider
from methods.userimagespider import userimagespider
from methods.usernamespider import namespider
from methods.searchspider import searchlist
#全局变量
offset = random.randint(0, 100)
favoriteclicknumber = 0
uploadclicknumber = 0
fastmodeclick = 0
indexuserfont = userdatas.indexuserfont
fontpathconfig = userdatas.fontpath
indexuserimage = userdatas.indexuserimage
imagefonconfig = userdatas.imagepath
downloadconfig = userdatas.downloadpathconfig
indexuserdownloadpath = userdatas.indexuserdownloadpath
cookiesconfig = userdatas.cookiesconfig
cookiescode = userdatas.cookiescode
if cookiescode == "" or cookiescode == "False":
    name = ""
    cookiescode = ""
    login = False
else:
    name = namespider(cookies=cookiescode).name
    indexuserimage = userimagespider(cookies=cookiescode).finallyresult
    login = True
if userdatas.iffastmodeopen == "True":
    fastmodeclose = 0
    indexfastmodeconfig = True
else:
    fastmodeclose = 1
    indexfastmodeconfig = False
#主页面
def main(page: ft.Page):
    page.title = "Watching"
    page.padding = 30
    page.window_center()
    page.window_frameless = True
    page.window_resizable = True
    page.window_height = 800
    page.window_width = 1298
    homeimageurllist = homespider().homeimageurl
    favoriteurllist = favoritespider(cookies=cookiescode).favoriteurl
    if indexuserfont == "微软雅黑":
        page.theme = ft.Theme(font_family=indexuserfont)
    else:
        page.fonts = {
            "userfont": indexuserfont
        }
        page.theme = ft.Theme(font_family="userfont")
    
    #函数与方法
    def CloseWarning(e):
        UserDatasChange(filepath=userdatas.warningconfig, value="True")
        warninginforview.open = False
        page.update()
        fasttips.open = True
        fasttips.update()

    def Favorite(e):
        if cookiescode == "":
            page.dialog = loginview
            loginview.open = True
            page.update()
        else:
            global favoriteclicknumber
            favoriteclicknumber += 1
            if favoriteclicknumber % 2 != 0:
                appbartoolip.value = "收藏"
                openfavoritebutton.tooltip = "返回首页"
                openfavoritebutton.icon = ft.icons.KEYBOARD_BACKSPACE_OUTLINED
                imageview.controls.clear()
                ImageView(list=favoriteurllist, view=imageview, download=indexuserdownloadpath)
                addbutton.visible = False
                homebutton.disabled = True
                searchtextfield.value = ""
                appbartoolip.update()
                imageview.update()
                page.update()
            else:
                appbartoolip.value = "发现"
                openfavoritebutton.tooltip = "收藏"
                imageview.controls.clear()
                ImageView(list=homeimageurllist, view=imageview, download=indexuserdownloadpath)
                openfavoritebutton.icon = ft.icons.FAVORITE_OUTLINE
                addbutton.visible = True
                appbartoolip.update()
                page.update()

    def DownFolder(e):
        subprocess.Popen(["Explorer", userdatas.downloadpath])

    def Search(e):
        appbartoolip.value = "搜索结果"
        page.floating_action_button = searchmorebutton
        searchmorebutton.visible = True
        addbutton.visible = False
        homebutton.disabled = False
        homebutton.update()
        imageview.clean()
        ImageView(view=imageview, list=searchlist(searchvalue=searchtextfield.value, offset=offset).spider,
                  download=indexuserdownloadpath)
        page.update()

    def BackHome(e):
        appbartoolip.value = "发现"
        page.floating_action_button = addbutton
        searchtextfield.value = ""
        addbutton.visible = True
        homebutton.disabled = True
        appbartoolip.update()
        homebutton.update()
        imageview.clean()
        ImageView(view=imageview, list=homeimageurllist, download=indexuserdownloadpath)
        page.update()

    def UpLoad(e):
        imageview.controls.clear()
        ImageView(list=homespider().homeimageurl, view=imageview, download=indexuserdownloadpath)
        homebutton.disabled = True
        searchtextfield.value = ""
        page.update()

    def Setting(e):
        page.dialog = settingview
        settingview.open = True
        page.update()

    def CloseSetting(e):
        settingview.open = False
        page.update()
        if fastmodebutton.value == True and fastmodeclose != 0:
            fasttips.open = True
            fasttips.update()
        elif fastmodebutton.value == False and fastmodeclose != 1:
            fasttips.open = True
            fasttips.update()
        else:
            pass

    def FastMode(e):
        global fastmodeclick
        fastmodeclick = fastmodeclick + 1
        if indexfastmodeconfig == True:
            if fastmodeclick % 2 != 0:
                UserDatasChange(filepath=userdatas.fastmodeconfig, value="False")
                fastmodebutton.value = False
                page.update()
            else:
                UserDatasChange(filepath=userdatas.fastmodeconfig, value="True")
                fastmodebutton.value = True
                page.update()
        else:
            if fastmodeclick % 2 != 0:
                UserDatasChange(filepath=userdatas.fastmodeconfig, value="True")
                fastmodebutton.value = True
                page.update()
            else:
                UserDatasChange(filepath=userdatas.fastmodeconfig, value="False")
                fastmodebutton.value = False
                page.update()

    def FontUpLoad(e: ft.FilePickerResultEvent):
        if e.files:
            fontname = ", ".join(map(lambda f: f.name, e.files))
            fontpath = ", ".join(map(lambda m: m.path, e.files))
            UserDatasChange(filepath=fontpathconfig, value=fontpath)
            indexfontview.value = (fontname[0:-4])
            page.fonts = {
                fontname: fontpath,
            }
            page.theme = ft.Theme(font_family=fontname)
            indexfontview.update()
            page.update()
        else:
            pass

    def UserImageUpLoad(e: ft.FilePickerResultEvent):
        global indexuserimage
        if e.files:
            userimagepath = ", ".join(map(lambda m: m.path, e.files))
            UserDatasChange(filepath=imagefonconfig, value=userimagepath)
            settingview.open = False
            page.update()
            fasttips.open = True
            fasttips.update()
        else:
            pass

    def DownLoadPathChange(e: ft.FilePickerResultEvent):
        if e.path:
            indexdownloadview.value = e.path
            UserDatasChange(filepath=downloadconfig, value=e.path)
            indexdownloadview.update()
            page.update()
        else:
            pass

    # 恢复默认设置
    def SettingBack(e):  
        fastmodebutton.value = False
        indexfontview.value = Defaultconfig.defaultfontpath
        indexdownloadview.value = Defaultconfig.defaultrdownloadpath
        UserDatasChange(filepath=userdatas.fastmodeconfig, value=Defaultconfig.defaultfastmodconfig)
        UserDatasChange(filepath=userdatas.imagepath, value=Defaultconfig.defaultimagepath)
        UserDatasChange(filepath=userdatas.downloadpathconfig, value=Defaultconfig.defaultrdownloadpath)
        UserDatasChange(filepath=userdatas.fontpath, value=Defaultconfig.defaultfontpath)
        page.theme = ft.Theme(font_family=indexuserfont)
        indexfontview.update()
        indexdownloadview.update()
        settingview.open = False
        page.update()
        fasttips.open = True
        fasttips.update()

    def LogIn(e):
        if cookiescode == "":
            page.dialog = loginview
            loginview.open = True
            page.update()
        else:
            page.dialog = userloginedview
            userloginedview.open = True
            page.update()

    def CloseLoginOK(e):
        if usercookiescode.value != "":
            global cookiescode
            cookiescode = usercookiescode.value
            UserDatasChange(filepath=cookiesconfig, value=usercookiescode.value)
            loginview.open = False
            page.update()
            tips.open = True
            tips.update()
        else:
            loginview.open = False
            page.update()
            tips2.open = True
            tips2.update()

    def CloseTips(e):
        tips2.open = False
        tips2.update()

    def Reboot(e):
        page.window_close()
        
    def CloseLogin(e):
        loginview.open = False
        page.update()
        tips2.open = True
        tips2.update()

    def ShowMore(e):
        if indexfastmodeconfig == True:
            imageview.clean()
            ImageView(view=imageview, list=homespider().homeimageurl, download=indexuserdownloadpath)
            page.update()
        else:
            ImageView(view=imageview, list=homespider().homeimageurl, download=indexuserdownloadpath)
            page.update()

    def SearchMore(e):
        global offset
        offset = offset + 10
        print(offset)
        if indexfastmodeconfig == "True":
            imageview.clean()
            ImageView(view=imageview, list=searchlist(searchvalue=searchtextfield.value, offset=offset).spider,
                      download=indexuserdownloadpath)
            page.update()
        else:
            ImageView(view=imageview, list=searchlist(searchvalue=searchtextfield.value, offset=offset).spider,
                      download=indexuserdownloadpath)
            page.update()

    def SignOut(e):
        UserDatasChange(filepath=userdatas.cookiesconfig, value="")
        userloginedview.open = False
        page.update()
        fasttips.open = True
        fasttips.update()

    def Close(e):
        page.window_close()

    def Link(e):
        cloumnview.controls.clear()
        page.dialog = linkview
        linkview.open = True
        page.update()
    
    def GetLink(e):
        cloumnview.controls.clear()
        ImageView(view=cloumnview, list=imageurllist(str=requests.get(linktextfield.value).text).imageurllist,download=indexuserdownloadpath)
        linktextfield.value = ""
        page.update()
    
    def CloseLinkView(e):
        linkview.open = False
        page.update()

    ####单独控件
    #用户头像
    if indexuserimage == "":
        userimage = appbarbutton(icon=ft.icons.SUPERVISED_USER_CIRCLE,event=LogIn,tooltip="登录").appbarbutton
    else:
        userimage = ft.Image(
            width=25,
            height=25,
            src=indexuserimage,
            fit=ft.ImageFit.COVER,
            border_radius=ft.border_radius.all(20),
        )
    
    userimagebutton = ft.Container(
        margin=ft.margin.only(left=10),
        on_click=LogIn,
        content=ft.Container(
            content=userimage
        ),
        tooltip="登录"
    )  

    #上传文件所需控件
    fontchange = ft.FilePicker(on_result=FontUpLoad)
    userimagechange = ft.FilePicker(on_result=UserImageUpLoad)
    downloadpathchange = ft.FilePicker(on_result=DownLoadPathChange)
    #登录框
    usercookiescode = ft.TextField(
        height=60,
        width=400,
        hint_text="cookies:",
    )
    
    #连接解析容器
    cloumnview = viewalone().view
    #控件
    fastmodebutton = ft.Switch(value=bool(indexfastmodeconfig), on_change=FastMode)
    indexfontview = ft.Text(indexuserfont)
    loginview = loginalone(usercookiescode=usercookiescode,closeloginok=CloseLoginOK,closelogin=CloseLogin).loginview
    userloginedview = userloginedalone(indexuserimage=indexuserimage,name=name,signout=SignOut).userloginedview
    homebutton = appbarbutton(icon=ft.icons.HOME,event=BackHome,tooltip="返回首页").appbarbutton
    uploadbutton = appbarbutton(icon=ft.icons.REFRESH,event=UpLoad,tooltip="刷新").appbarbutton
    opendownloadbutton = appbarbutton(icon=ft.icons.FOLDER_OUTLINED,event=DownFolder,tooltip="打开下载文件夹").appbarbutton
    closebutton = appbarclosebutton(icon=ft.icons.CLOSE,event=lambda _: page.window_close()).appbarbutton
    openfavoritebutton = appbarbutton(icon=ft.icons.FAVORITE_OUTLINE,event=Favorite,tooltip="收藏").appbarbutton
    settingbutton = appbarbutton(icon=ft.icons.SETTINGS,event=Setting,tooltip="设置").appbarbutton
    linkbutton = appbarbutton(icon=ft.icons.INSERT_LINK,event=Link,tooltip="解析链接").appbarbutton
    linktextfield = linktext(event=lambda e: GetLink(e.control.value)).linktextfield
    linkview = linkalone(closelinkview=CloseLinkView,cloumnview=cloumnview,linktextfield=linktextfield).linkview
    indexdownloadview = ft.Text(indexuserdownloadpath)
    settingview = SettingAlone(fastmodebutton=fastmodebutton,indexdownloadview=indexdownloadview,downloadpathchange=downloadpathchange,indexfontview=indexfontview,fontchange=fontchange,userimagechange=userimagechange,settingback=SettingBack,closesetting=CloseSetting).settingview
    searchtextfield = searchalone(event=lambda e: Search(e.control.value)).searchtextfield
    homebutton.disabled = True
    
    #AppBar
    appbartoolip = ft.Text(
        "发现",
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(
            size=18,
        )
    )
    page.appbar = appbar(
        view=appbartoolip,
        title=searchtextfield,
        controls=[
            homebutton,
            uploadbutton,
            linkbutton,
            opendownloadbutton,
            openfavoritebutton,
            settingbutton,
            userimagebutton,
            closebutton,
        ]
    ).appbar

    # 悬浮按钮
    addbutton = floatbutton(event=ShowMore).floatbutton
    searchmorebutton = floatbutton(event=SearchMore).floatbutton

    #首次启动警告
    warninginforview = warningalone(close=Close,closewarning=CloseWarning).warninginforview
    if userdatas.warningmode == "False":
        page.dialog = warninginforview
        warninginforview.open = True
        page.update()
    else:
        pass

    #图片容器
    imageview = gridviewalone().imageview
    
    #提示信息
    tips = tipsview(title="登录成功，点击重启软件后生效",text="点击重启",margin=300,event=Reboot).tipsview
    fasttips = tipsview(title="修改成功，点击重启软件后生效",text="点击重启",margin=300,event=Reboot).tipsview
    tips2 = tipsview(title="登录无效",text="关闭提示",margin=450,event=CloseTips).tipsview
    page.overlay.append(tips)
    page.overlay.append(tips2)
    page.overlay.append(fasttips)

    #显示页面
    ImageView(list=homeimageurllist, view=imageview, download=indexuserdownloadpath)
    page.floating_action_button = addbutton
    page.update()
    page.add(
        imageview,
        fontchange,
        userimagechange,
        downloadpathchange,

    )

ft.app(target=main)