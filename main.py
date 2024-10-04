import flet as ft


class Header_link:
    def __init__(self, text):
        self.text_label = ft.Container(
            ft.Text(text,
                    theme_style=ft.TextThemeStyle.BODY_SMALL,
                    text_align=ft.TextAlign.CENTER),
            padding=5,
            # bgcolor=ft.colors.GREY_900,
            col={"sm": 6, "md": 4, "xl": 2},
        )


class TextParagraph:
    def __init__(self, text_par):
        self.text_paragraph = ft.Text(value=text_par, col={"md": 6}, text_align=ft.TextAlign.CENTER,
                                      max_lines=10, expand=True, width=200, height=400)


def main(page: ft.Page):

    def open_google(e):
        page.launch_url("https://google.com")

    def open_seznam(e):
        page.launch_url("https://seznam.cz")

    def open_root(e):
        page.launch_url("https://root.cz")

    class MyTextButton:

        def __init__(self, btn_text: str, function):
            self.link_button_container = ft.Container(
                ft.TextButton(text=btn_text, on_click=function,
                              style=ft.ButtonStyle(color=ft.colors.WHITE)),
                padding=5,
                col={"sm": 6, "md": 4, "xl": 2},
            )

    def page_resize(e):
        pw.value = f"{page.width} px"
        pw.update()

    page.on_resize = page_resize
    page.scroll = True
    page.theme_mode = ft.ThemeMode.DARK

    pw = ft.Text(bottom=50, right=50, style="displaySmall")
    page.overlay.append(pw)

    page.add(
        ft.ResponsiveRow(
            [
                MyTextButton("Contact", open_google).link_button_container,
                MyTextButton("LinkedIn", open_google).link_button_container,
                MyTextButton("Micro projects", open_google).link_button_container,
                MyTextButton("Blog", open_google).link_button_container,
                MyTextButton("My text btn 1", open_seznam).link_button_container,
            ],
        ),
        ft.ResponsiveRow(
            [
                TextParagraph("\n\n\nTextField 1\nTextField 2\nTextField 3\n").text_paragraph,
                TextParagraph("\n\n\nTextField 1\nTextField 2\nTextField 3\n").text_paragraph,
                TextParagraph("\n\n\nTextField 1\nTextField 2\nTextField 3\n").text_paragraph,
                TextParagraph("\n\n\nTextField 1\nTextField 2\nTextField 3\n").text_paragraph,
                TextParagraph("\n\n\nTextField 1\nTextField 2\nTextField 3\n").text_paragraph,
            ],
            run_spacing={"xs": 10},
        ),
    )
    page_resize(None)


# ft.app(main)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
