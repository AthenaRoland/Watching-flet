import flet as ft

class AlertDialog:
    def __init__(self,title,controls,width,height,modal,actions,alignment):
        self.alertdialog = ft.AlertDialog(
            modal=modal,
            title=ft.Text(f"{title}"),
            content=ft.Column(
                alignment=alignment,
                width=width,
                height=height,
                controls=controls
            ),
            actions=actions,
            actions_alignment=ft.MainAxisAlignment.END
        )

class AppBarCloseButton():
    def __init__(self,icon,event):
        self.appbarbutton = ft.IconButton(
            icon=icon,
            on_click=event,
            icon_size=25,
            width=50,
        )

class AppBarButton():
    def __init__(self,icon,event,tooltip):
        self.appbarbutton = ft.IconButton(
            icon=icon,
            on_click=event,
            icon_size=25,
            width=30,
            tooltip=tooltip
        )

class TipsView:
    def __init__(self,title,text,event,margin):
        self.tipsview = ft.BottomSheet(
            content=ft.Container(
                padding=20,
                content=ft.Row(
                    controls=[
                        ft.Text(
                            f"{title}",
                            style=ft.TextStyle(
                                size=15
                            )
                        ),
                        ft.Container(
                            margin=ft.margin.only(left=margin),
                            content=ft.TextButton(
                                content=ft.Container(
                                    content=ft.Text(
                                        f"{text}",
                                        style=ft.TextStyle(
                                            size=15
                                        )
                                    )
                                ),
                                on_click=event
                            )
                        )
                    ]
                )
            )
        )

class FloatButton:
    def __init__(self,event):
        self.floatbutton = ft.FloatingActionButton(
            icon=ft.icons.ADD,
            on_click=event,
            bgcolor=ft.colors.BLUE_300,
            shape=ft.RoundedRectangleBorder(radius=30),
            tooltip="加载更多图片"
        )

class AppBar:
    def __init__(self,view,title,controls):
        self.appbar = ft.AppBar(
            leading=ft.WindowDragArea(
                content=ft.Container(
                    width=450,
                    alignment=ft.alignment.center_left,
                    content=ft.Row(
                        controls=[
                            ft.Text(" "),
                            view
                        ]
                    ),
                ),
            ),
            leading_width=300,
            center_title=True,
            title=ft.Row(
                controls=[title],

            ),
            toolbar_height=45,
            actions=[
                ft.Row(controls=controls)
            ],
        )

appbar = AppBar
floatbutton = FloatButton
tipsview = TipsView
appbarclosebutton = AppBarCloseButton
appbarbutton = AppBarButton
alertdialog = AlertDialog