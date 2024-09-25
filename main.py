import flet as ft


class Header_link():
    def __init__(self, text):
        self.text_label = header_container = ft.Container(
            ft.Text(text,
                    theme_style=ft.TextThemeStyle.BODY_SMALL,
                    text_align=ft.TextAlign.CENTER),
            padding=5,
            #bgcolor=ft.colors.GREY_900,
            col={"sm": 6, "md": 4, "xl": 2},
        )


def main(page: ft.Page):
    def page_resize(e):
        pw.value = f"{page.width} px"
        pw.update()

    page.on_resize = page_resize

    pw = ft.Text(bottom=50, right=50, style="displaySmall")
    page.overlay.append(pw)

    page.add(
        ft.ResponsiveRow(
            [
                Header_link("Contact me").text_label,
                Header_link("linketIn profile").text_label,
                Header_link("micro projects").text_label,
                Header_link("blog").text_label,
                Header_link("something 1").text_label,
                Header_link("something 2").text_label,
            ],
        ),
        ft.ResponsiveRow(
            [
                ft.TextField(label="TextField 1", col={"md": 6}),
                ft.TextField(label="TextField 2", col={"md": 6}),
                ft.TextField(label="TextField 3", col={"md": 6}),
                ft.TextField(label="TextField 4", col={"md": 6}),
            ],
            run_spacing={"xs": 10},
        ),
    )
    page_resize(None)


ft.app(main)
