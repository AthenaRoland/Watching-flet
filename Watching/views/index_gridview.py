import flet as ft
import requests

downloadpath = ""


class ImageView():
    def __init__(self, view, list, download):
        global downloadpath
        downloadpath = download
        for content in list:
            image = ft.Container(
                padding=10,
                content=ft.Column(
                    controls=[
                        ft.Image(
                            width=600,
                            height=350,
                            src=content,
                            fit=ft.ImageFit.FIT_WIDTH,
                            repeat=ft.ImageRepeat.REPEAT_X,
                            border_radius=ft.border_radius.all(15),
                        ),
                        ft.Row(
                            width=600,
                            controls=[
                                ft.Container(
                                    # width=300,
                                    margin=ft.margin.only(left=550),
                                    content=ft.IconButton(
                                        icon=ft.icons.DOWNLOAD,
                                        on_click=self.Download(i=content),
                                        icon_size=20,
                                        tooltip="下载图片"
                                    )
                                )
                            ]
                        )
                    ]
                )
            )
            view.controls.append(image)

    def Download(e, i):
        def download(value):
            value = i
            name = value[-18:]
            r = requests.get(value)
            with open(f"{downloadpath}" + r"\\" + f"{name}", "wb") as f:
                f.write(r.content)

        return download
