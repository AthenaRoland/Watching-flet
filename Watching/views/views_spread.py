import flet as ft
from views.views import *

class WarningAlone:
    def __init__(self,closewarning,close):
        self.warninginforview = alertdialog(
            modal=True,
            title="用户须知",
            width=400,
            height=200,
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
                    padding=10,
                    content=ft.Text(
                        text_align=ft.TextAlign.CENTER,
                        value="2.图片来源于Lofter,请尊重作者版权,切勿用于商业用途,图片只供个人学习交流.",
                        style=ft.TextStyle(
                            size=15
                        )
                    )
                )
            ],
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
                    on_click=closewarning
                ),
                ft.TextButton(
                    content=ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Text(
                            "取消并关闭程序",
                            style=ft.TextStyle(
                                size=15,
                            )
                        )
                    ),
                    on_click=close
                )
            ],
            alignment=None,
        ).alertdialog
        

class SettingAlone:
    def __init__(self,fastmodebutton,indexdownloadview,downloadpathchange,indexfontview,fontchange,userimagechange,settingback,closesetting):
        self.settingview = ft.AlertDialog(
            modal=True,
            title=ft.Text("设置"),
            content=ft.ListView(
                height=350,
                width=500,
                controls=[
                    ft.ListTile(
                        leading=ft.Text("主题设置", style=ft.TextStyle(size=15)),
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
                        leading=ft.Text("流畅模式", style=ft.TextStyle(size=15)),
                        trailing=ft.MenuBar(
                            expand=True,
                            controls=[
                                fastmodebutton
                            ]
                        )
                    ),
                    ft.ListTile(
                        leading=ft.Text("下载路径", style=ft.TextStyle(size=15)),
                        title=indexdownloadview,
                        trailing=ft.IconButton(
                            ft.icons.DRIVE_FILE_RENAME_OUTLINE_OUTLINED,
                            on_click=lambda _: downloadpathchange.get_directory_path()
                        )
                    ),
                    ft.ListTile(
                        leading=ft.Text("字体设置", style=ft.TextStyle(size=15)),
                        title=indexfontview,
                        trailing=ft.IconButton(
                            ft.icons.DRIVE_FILE_RENAME_OUTLINE_OUTLINED,
                            on_click=lambda _: fontchange.pick_files(allowed_extensions=["ttf"])
                        )
                    ),
                    ft.ListTile(
                        leading=ft.Text("用户头像", style=ft.TextStyle(size=15)),
                        trailing=ft.IconButton(
                            ft.icons.FILE_UPLOAD_OUTLINED,
                            on_click=lambda _: userimagechange.pick_files(allowed_extensions=["jpg", "png", "jpeg"])
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
                    on_click=settingback,
                ),
                ft.TextButton(
                    content=ft.Text(
                        "确定",
                        style=ft.TextStyle(
                            size=15
                        )
                    ),
                    on_click=closesetting,
                ),
                ft.TextButton(
                    content=ft.Text(
                        "关闭",
                        style=ft.TextStyle(
                            size=15
                        )
                    ),
                    on_click=closesetting,
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

class LoginAlone:
    def __init__(self,usercookiescode,closeloginok,closelogin):
        self.loginview = alertdialog(
            modal=True,
            title="登录",
            height=300,
            width=450,
            controls=[
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Image(
                        src=r".\assets\images\login.png",
                        width=150,
                        height=60
                    )
                ),
                ft.Container(
                    padding=40,
                    alignment=ft.alignment.center,
                    content=usercookiescode
                )
            ],
            actions=[
                ft.TextButton(
                    content=ft.Text(
                        "登录",
                        style=ft.TextStyle(
                            size=15
                        )
                    ),
                    on_click=closeloginok,
                ),
                ft.TextButton(
                    content=ft.Text(
                        "取消",
                        style=ft.TextStyle(
                            size=15
                        )
                    ),
                    on_click=closelogin,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ).alertdialog

class UserLoginedAlone:
    def __init__(self,indexuserimage,name,signout):
        self.userloginedview = ft.AlertDialog(
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
                                on_click=signout
                            )
                        )
                    )
                ]
            )
        )

class GridViewAlone:
    def __init__(self):
        self.imageview = ft.GridView(
            expand=1,
            runs_count=2,
            child_aspect_ratio=1.48,
            run_spacing=5,
        )
    
class ViewAlone:
    def __init__(self):
        self.view = ft.Column()

class SearchAlone:
    def __init__(self,event):
        self.searchtextfield = ft.TextField(
            label="在此处搜索...",
            label_style=ft.TextStyle(
                size=15,
            ),
            suffix_icon=ft.icons.SEARCH,
            width=600,
            height=32,
            cursor_height=15,
            text_size=12,
            on_submit=event
        )

class LinkText:
    def __init__(self,event):
        self.linktextfield = ft.TextField(
            hint_text="链接:",
            text_align=ft.TextAlign.LEFT,
            hint_style=ft.TextStyle(
                size=15
            ),
            on_submit=event,
            height=45,
            cursor_height=30,
            text_size=18,
        )

class LinkAlone:
    def __init__(self,closelinkview,cloumnview,linktextfield):
        self.linkview = ft.AlertDialog(
            modal=False,
            title=ft.Text("解析结果"),
            content=ft.ListView(
                height=450,
                width=620,
                controls=[
                    ft.Container(
                        padding=10,
                        content=linktextfield
                    ),
                    cloumnview
                ]
            ),
            actions=[
                ft.TextButton(
                    content=ft.Text(
                        "关闭",
                        style=ft.TextStyle(
                            size=18
                        )
                    ),
                    on_click=closelinkview,
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
warningalone = WarningAlone
settingalone = SettingAlone
loginalone = LoginAlone
userloginedalone = UserLoginedAlone
gridviewalone = GridViewAlone
searchalone = SearchAlone
linkalone = LinkAlone
viewalone = ViewAlone
linktext = LinkText