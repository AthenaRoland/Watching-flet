import flet as ft
import subprocess
import random
from views.index_gridview import ImageView
from methods.userdatasread import userdatas
from methods.userdataschange import UserDatasChange
from methods.default import Defaultconfig
from methods.iamgespider import homespider
from methods.favoritespider import favoritespider
from methods.userimagespider import userimagespider
from methods.usernamespider import namespider
from methods.searchspider import searchlist

#全局变量
offset = random.randint(0,100)
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
warningmode = userdatas.warningmode
warningconfig = userdatas.warningconfig
if cookiescode == "" or cookiescode == "False":
    name = ""
    cookiescode = ""
    login = False
else:
    name=namespider(cookies=cookiescode).name
    indexuserimage = userimagespider(cookies=cookiescode).finallyresult
    login = True
if userdatas.iffastmodeopen == "True":
    fastmodeclose = 0
    indexfastmodeconfig = True
    print(indexfastmodeconfig)
    print(fastmodeclose)
else:
    fastmodeclose = 1
    indexfastmodeconfig = False


def main(page: ft.Page):
    #基础配置
    page.padding = 30
    page.window_center()
    page.window_frameless = True
    page.window_resizable = True
    page.window_height = 800
    page.window_width = 1298
    if indexuserfont == "微软雅黑":
        page.theme = ft.Theme(font_family=indexuserfont)
    else:
        page.fonts = {
            "userfont":indexuserfont
        }
        page.theme = ft.Theme(font_family="userfont")
    homeimageurllist = homespider().homeimageurl
    favoriteurllist = favoritespider(cookies=cookiescode).favoriteurl

    #函数部分
    def CloseWarning(e):
        UserDatasChange(filepath=warningconfig,value="True")
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
                ImageView(list=favoriteurllist, view = imageview, download=indexuserdownloadpath)
                addbutton.visible = False
                appbartoolip.update()
                addbutton.update()
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
                addbutton.update()
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
        ImageView(view=imageview,list=searchlist(searchvalue=searchtextfield.value,offset=offset).spider,download=indexuserdownloadpath)
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
        ImageView(view=imageview,list=homeimageurllist,download=indexuserdownloadpath)
        page.update()

    def UpLoad(e):
        global uploadclicknumber
        uploadclicknumber += 1
        if uploadclicknumber % 2 != 0:
            imageview.controls.clear()
            ImageView(list=homespider().homeimageurl, view=imageview,download=indexuserdownloadpath)
            page.update()
        else:
            pass
    
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
                page.update
            else:
                UserDatasChange(filepath=userdatas.fastmodeconfig, value="True")
                fastmodebutton.value = True
                page.update
        else:
            if fastmodeclick % 2 != 0:
                UserDatasChange(filepath=userdatas.fastmodeconfig, value="True")
                fastmodebutton.value = True
                page.update
            else:
                UserDatasChange(filepath=userdatas.fastmodeconfig, value="False")
                fastmodebutton.value = False
                page.update

    def FontUpLoad(e: ft.FilePickerResultEvent):                        #上传字体函数
        if e.files:
            fontname = ", ".join(map(lambda f: f.name, e.files))        #字体名称
            fontpath = ", ".join(map(lambda m: m.path, e.files))       #字体路径
            UserDatasChange(filepath=fontpathconfig, value=fontpath)
            print(fontpath)
            indexfontview.value = (fontname[0:-4])
            page.fonts = {
                fontname: fontpath,
            }
            page.theme = ft.Theme(font_family=fontname)
            indexfontview.update()
            page.update()
        else:
            pass
    fontchange = ft.FilePicker(on_result=FontUpLoad)     #上传字体

    def UserImageUpLoad(e: ft.FilePickerResultEvent):
        if e.files:
            userimagepath = ", ".join(map(lambda m: m.path, e.files))
            userimage.src = userimagepath
            print(userimagepath)
            UserDatasChange(filepath=imagefonconfig,value=userimagepath)
            userimage.update()
            userimagebutton.update()
            page.update()
        else:
            pass
    userimagechange = ft.FilePicker(on_result=UserImageUpLoad)

    def DownLoadPathChange(e: ft.FilePickerResultEvent):
        if e.path:
            indexdownloadview.value = e.path
            UserDatasChange(filepath=downloadconfig, value=e.path)
            indexdownloadview.update()
            page.update()
        else:
            pass
    downloadpathchange = ft.FilePicker(on_result=DownLoadPathChange)
    
    def SettingBack(e):                                                #恢复默认设置
        fastmodebutton.value = False
        indexfontview.value = Defaultconfig.defaultfontpath
        indexdownloadview.value = Defaultconfig.defaultrdownloadpath
        UserDatasChange(filepath=userdatas.fastmodeconfig,value=Defaultconfig.defaultfastmodconfig)
        UserDatasChange(filepath=userdatas.imagepath,value=Defaultconfig.defaultimagepath)
        UserDatasChange(filepath=userdatas.downloadpathconfig,value=Defaultconfig.defaultrdownloadpath)
        UserDatasChange(filepath=userdatas.fontpath,value=Defaultconfig.defaultfontpath)
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
            UserDatasChange(filepath=cookiesconfig,value=usercookiescode.value)
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
            ImageView(view=imageview, list=searchlist(searchvalue=searchtextfield.value,offset=offset).spider,download=indexuserdownloadpath)
            page.update()
        else:
            ImageView(view=imageview, list=searchlist(searchvalue=searchtextfield.value,offset=offset).spider,download=indexuserdownloadpath)
            page.update()
    
    def SignOut(e):
        UserDatasChange(filepath=userdatas.cookiesconfig,value="")
        userloginedview.open = False
        page.update()
        fasttips.open = True
        fasttips.update()

    def Close(e):
        page.window_close()

    #单独控件部分
    searchtextfield = ft.TextField(
        label="在此处搜索...",
        label_style=ft.TextStyle(
            size=15,
        ),
        suffix_icon=ft.icons.SEARCH,
        width=600,
        height=32,
        cursor_height = 15,
        text_size = 12,
        on_submit=lambda e: Search(e.control.value)
    )
    tips = ft.BottomSheet(
            content=ft.Container(
                padding=20,
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "登录成功，点击重启软件后生效",
                            style=ft.TextStyle(
                                size=15
                            )
                        ),
                        ft.Container(
                            margin=ft.margin.only(left=300),
                            content=ft.TextButton(
                                content=ft.Container(
                                    content=ft.Text(
                                        "点击重启",
                                        style=ft.TextStyle(
                                            size=15
                                        )
                                    )
                                ),
                                on_click=lambda _: page.window_close()
                            )
                        )
                    ]
                )
            )
    )
    fasttips = ft.BottomSheet(
            content=ft.Container(
                padding=20,
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "修改成功，点击重启软件后生效",
                            style=ft.TextStyle(
                                size=15
                            )
                        ),
                        ft.Container(
                            margin=ft.margin.only(left=300),
                            content=ft.TextButton(
                                content=ft.Container(
                                    content=ft.Text(
                                        "点击重启",
                                        style=ft.TextStyle(
                                            size=15
                                        )
                                    )
                                ),
                                on_click=lambda _: page.window_close()
                            )
                        )
                    ]
                )
            )
    )
    tips2 = ft.BottomSheet(
            content=ft.Container(
                padding=20,
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "登录无效",
                            style=ft.TextStyle(
                                size=15
                            )
                        ),
                        ft.Container(
                            margin=ft.margin.only(left=450),
                            content=ft.TextButton(
                                content=ft.Container(
                                    content=ft.Text(
                                        "关闭提示",
                                        style=ft.TextStyle(
                                            size=15
                                        )
                                    )
                                ),
                                on_click=CloseTips
                            )
                        )
                    ]
                )
            )
    )
    fastmodebutton = ft.Switch(value=bool(indexfastmodeconfig),on_change=FastMode)
    usercookiescode = ft.TextField(
                        height=60,
                        width=400,
                        hint_text="cookies:",
                    )
    loginview = ft.AlertDialog(
        modal=True,
        title=ft.Text("登录"),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            height=300,
            width=450,
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Image(
                        src=r".\sources\images\login.png",
                        width=150,
                        height=60
                    )
                ),
                ft.Container(
                    padding=40,
                    alignment=ft.alignment.center,
                    content=usercookiescode
                )
            ]
        ),
        actions=[
            ft.TextButton(
                content=ft.Text(
                    "登录",
                    style=ft.TextStyle(
                        size=15
                    )
                ),
                on_click=CloseLoginOK,
            ),
            ft.TextButton(
                content=ft.Text(
                    "取消",
                    style=ft.TextStyle(
                        size=15
                    )
                ), 
                on_click=CloseLogin,
            )
            ],
            actions_alignment=ft.MainAxisAlignment.END,
    )
    
    userloginedview = ft.AlertDialog(
            title=ft.Text("已登录"),
            content=ft.Column(
                width=150,
                height=200,
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Image(
                            width=100,
                            height=100,
                            src=indexuserimage,
                            fit=ft.ImageFit.FILL,
                            border_radius=ft.border_radius.all(100),  
                        )
                    ),
                    ft.Container(
                        padding=10,
                        alignment=ft.alignment.center,
                        content=ft.Text(
                            f"{name}",
                            style=ft.TextStyle(
                                size=20
                            )
                        )
                    ),
                    ft.Container(
                        padding=10,
                        alignment=ft.alignment.center,
                        content=ft.TextButton(
                            content=ft.Container(
                                content=ft.Text(
                                    "退出登录",
                                    style=ft.TextStyle(
                                        size=15
                                    )
                                ),
                                on_click=SignOut
                            )
                        )
                    )
                ]
            )
        )
    
    indexfontview = ft.Text(indexuserfont)                                            #字体设置提示信息控件

    homebutton = ft.IconButton(
        ft.icons.HOME,
        on_click=BackHome,
        icon_size=25,
        width=30,
        tooltip="返回首页",
        disabled=True
    )

    uploadbutton = ft.IconButton(                                        #刷新按钮
                    ft.icons.REFRESH,
                    on_click=UpLoad,
                    icon_size=25,
                    width=30,
                    tooltip="刷新"
                )
    
    userimage = ft.Image(
            width=25,
            height=25,
            src=indexuserimage,
            fit=ft.ImageFit.COVER,
            border_radius=ft.border_radius.all(20),           
    )
    userimagebutton = ft.Container(                                      #用户头像
        on_click=LogIn,
        content=userimage,
        tooltip="登录"
    )
    
    opendownloadbutton = ft.IconButton(                                  #打开下载按钮
                    ft.icons.FOLDER_OUTLINED,
                    on_click=DownFolder,
                    icon_size=25,
                    width=30,
                    tooltip="打开下载文件夹"
                )
    

    openfavoritebutton = ft.IconButton(                                  #打开收藏按钮
                    ft.icons.FAVORITE_OUTLINE,
                    on_click=Favorite,
                    icon_size=25,
                    width=30,
                    tooltip="收藏"
                )
    
    closebutton = ft.IconButton(                                          #关闭程序按钮
                    ft.icons.CLOSE, 
                    on_click=lambda _: page.window_close(),
                    icon_size=25,
                    width=50,
                )
    
    settingbutton = ft.IconButton(                                        #打开设置按钮
                    ft.icons.SETTINGS, 
                    on_click=Setting,
                    icon_size=25,
                    width=35,
                    tooltip="设置"
                )
    
    indexdownloadview = ft.Text(indexuserdownloadpath)
    settingview = ft.AlertDialog(                                                           #设置页面
        modal=True,
        title=ft.Text("设置"),
        content=ft.ListView(
            height=350,
            width=500,
            controls=[
                ft.ListTile(                                                                #主题设置
                    leading=ft.Text("主题设置",style=ft.TextStyle(size=15)),
                    trailing=ft.MenuBar(
                        expand=True,
                        controls=[
                            ft.SubmenuButton(
                                height=30,
                                content=ft.Text("跟随系统"),
                                controls=[
                                    ft.MenuItemButton(
                                        content=ft.Text("跟随系统"),
                                        leading=ft.Icon(ft.icons.BRIGHTNESS_AUTO_OUTLINED),
                                    ),                                
                                ]
                            )
                        ]
                    )
                ),
                ft.ListTile(
                    leading=ft.Text("流畅模式",style=ft.TextStyle(size=15)),              #流畅模式
                    trailing=ft.MenuBar(
                        expand=True,
                        controls=[
                            fastmodebutton
                        ]
                    )
                ),
                ft.ListTile(                                                                #下载路径设置
                    leading=ft.Text("下载路径",style=ft.TextStyle(size=15)),
                    title=indexdownloadview,
                    trailing=ft.IconButton(
                        ft.icons.DRIVE_FILE_RENAME_OUTLINE_OUTLINED,
                        on_click=lambda _: downloadpathchange.get_directory_path()
                    )
                ),
                ft.ListTile(                                                                #字体设置
                    leading=ft.Text("字体设置",style=ft.TextStyle(size=15)),
                    title=indexfontview,
                    trailing=ft.IconButton(                                                 #选择字体
                                ft.icons.DRIVE_FILE_RENAME_OUTLINE_OUTLINED,
                                on_click=lambda _: fontchange.pick_files(allowed_extensions=["ttf"])
                    )  
                ),
                ft.ListTile(                                                                #用户头像设置
                    leading=ft.Text("用户头像",style=ft.TextStyle(size=15)),
                    trailing=ft.IconButton(
                        ft.icons.FILE_UPLOAD_OUTLINED,
                        on_click=lambda _: userimagechange.pick_files(allowed_extensions=["jpg","png","jpeg"])
                    )
                ), 
            ]
        ),
        actions=[
            ft.TextButton(
                content=ft.Text(
                    "恢复默认",
                    style=ft.TextStyle(
                        size=15
                    )
                ),
                on_click=SettingBack,
            ),
            ft.TextButton(
                content=ft.Text(
                    "确定",
                    style=ft.TextStyle(
                        size=15
                    )
                ),
                on_click=CloseSetting,
            ),
            ft.TextButton(
                content=ft.Text(
                    "关闭",
                    style=ft.TextStyle(
                        size=15
                    )
                ),
                on_click=CloseSetting,
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    appbartoolip = ft.Text(
        "发现",
        text_align=ft.TextAlign.CENTER,
        style=ft.TextStyle(
            size=18,
        )
    )

    #AppBar导航栏部分
    page.appbar = ft.AppBar(
        leading=ft.WindowDragArea(
            content=ft.Container(
                width=450,
                alignment=ft.alignment.center_left,
                content=ft.Row(
                    controls=[
                        ft.Text(" "),
                        appbartoolip
                    ]
                ),
            ),
        ),
        leading_width=300,
        center_title=True,
        title=ft.Row(
            controls=[
                searchtextfield
            ],

        ),
        toolbar_height=45,
        actions=[
            ft.Row([
                homebutton,
                uploadbutton,
                opendownloadbutton,
                openfavoritebutton,
                settingbutton,
                userimagebutton,
                closebutton,
            ])
        ],
    )
    #悬浮按钮
    addbutton = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        on_click=ShowMore, 
        bgcolor=ft.colors.BLUE_300,
        shape=ft.RoundedRectangleBorder(radius=30),
        tooltip="加载更多图片"
    )
    page.floating_action_button = addbutton

    searchmorebutton = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        on_click=SearchMore, 
        bgcolor=ft.colors.BLUE_300,
        shape=ft.RoundedRectangleBorder(radius=30),
        tooltip="加载更多图片"
    )
    
    warninginforview = ft.AlertDialog(
        title=ft.Text("用户须知"),
        content=ft.Container(
            width=400,
            height=200,
            content=ft.Column(
                controls=[
                    ft.Container(
                        margin=ft.margin.only(top=50),
                        content=ft.Text(
                            text_align=ft.TextAlign.CENTER,
                            value="  1.此软件为开源软件,完全免费,若你是购买的,那么你被骗了.",
                            style=ft.TextStyle(
                                size=15
                            )
                        )
                    ),
                    ft.Container(
                        padding = 10,
                        content=ft.Text(
                            text_align=ft.TextAlign.CENTER,
                            value="2.图片来源于Lofter,请尊重作者版权,切勿用于商业用途,图片只供个人学习交流.",
                            style=ft.TextStyle(
                                size=15
                            )
                        )
                    )
                ]
            )
        ),
        actions=[
                ft.TextButton(
                    content=ft.Container(
                            alignment=ft.alignment.center,
                            content=ft.Text(
                                "我已阅读并同意",
                                style=ft.TextStyle(
                                    size=15,
                                    color="yellow"
                                )
                            )
                        ),
                    on_click=CloseWarning
                ),
                ft.TextButton(
                    content = ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Text(
                            "取消并关闭程序",
                            style=ft.TextStyle(
                                size=15,
                            )
                        )
                    ),
                    on_click=Close
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END
    )
    

    if warningmode == "False":
        page.dialog = warninginforview
        warninginforview.open = True
        page.update()
    else:
        pass

    #发现/首页图片内容
    imageview = ft.GridView(
            expand=1,
            runs_count=2,
            child_aspect_ratio=1.48,#上下间距
            run_spacing=5,
        )
    ImageView(list=homeimageurllist, view=imageview, download=indexuserdownloadpath)
    page.update()
    page.overlay.append(tips)
    page.overlay.append(tips2)
    page.overlay.append(fasttips)
    page.add(
        imageview,
        fontchange,
        userimagechange,
        downloadpathchange,
        
    )
ft.app(target=main)