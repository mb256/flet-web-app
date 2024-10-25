import flet as ft
import asyncio


messages = [
    "Work smart not hard",
    "Assume you can learn something new from everyone",
    "Never disrespect your elders",
    "Don’t be scared of change, embrace it",
    "Live in the moment, not on your phone",
    "Always pay the bill",
    "Say no if you aren’t ready",
    "Present yourself in the way you wish to be perceived",
    "Mentally prepare yourself for your loved ones dying",
    "Never take rejection personally",
    "Don’t be embarrassed to take a nap",
    "Learn from those who disagree with you",
    "Never be late",
    "Be motivated by something greater than money",
    "Be fuelled by vision not fear",
    "Stand up to bullies",
]


class HeaderLink:
    def __init__(self, text):
        self.text_label = ft.Container(
            ft.Text(text,
                    theme_style=ft.TextThemeStyle.BODY_SMALL,
                    text_align=ft.TextAlign.CENTER),
            padding=5,
            # bgcolor=ft.colors.GREY_900,
            col={"sm": 6, "md": 4, "xl": 2},
        )


class DynamicTextOnBackground:
    def __init__(self, message_list: list, image_source: str):
        self.message_list = message_list
        self.index = 0
        self.message = ft.Text("", theme_style=ft.TextThemeStyle.HEADLINE_LARGE)

        self.content = ft.Container(
            self.message,
            alignment=ft.alignment.center,
            col={"md": 6},
            image=ft.DecorationImage(src=image_source, fit=ft.ImageFit.COVER),
            image_fit=ft.ImageFit.CONTAIN,
            expand=True,
            width=800,
            height=600,
        )

    async def update_message(self):
        await asyncio.sleep(1.5)
        # Iterate over all quotes
        while True:
            # Iterate over letters in one quotes
            for letter in self.message_list[self.index]:
                self.message.value = self.message.value + letter
                self.content.update()
                await asyncio.sleep(0.05)
            # Increment index so it takes another quote from the list
            # (% len() will set index back to '0' once we went through whole list
            self.index = (self.index + 1) % len(self.message_list)
            await asyncio.sleep(6)
            self.message.value = ""


class TextParagraph:
    def __init__(self, text_par):
        self.content = ft.Container(
            ft.Text(value=text_par, size=22, col={"md": 6}, text_align=ft.TextAlign.CENTER,
                    expand=True, width=200, height=400),
            #alignment=ft.alignment.center,
            col={"md": 6},
        )


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK

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

    pw = ft.Text(bottom=50, right=50, style="displaySmall")
    page.overlay.append(pw)

    page.on_resize = page_resize
    page.scroll = True
    page.theme_mode = ft.ThemeMode.DARK

    # Dynamic text on background
    background_image = DynamicTextOnBackground(messages, "/family_dark_dark_edge.jpg")
    page.run_task(background_image.update_message)

    main_info = TextParagraph("\n\n\n\n\n"
                              "15+ years of experience\n"
                              "in Software and Firmware development\n\n"
                              "Focus on (embedded) Linux platforms.\n"
                              "Years of experience in team leader position.\n\n"
                              "Technology stack:\n"
                              "Python, C, C++, Linux, ...")

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
                main_info.content,
                background_image.content,

                TextParagraph("\n\n\nBlog article 1\n\nBlog article 2\n\nBlog article 3\n").content,
                TextParagraph("\n\n\nMicro project 1\n\nMicro project 2\n\nMicro project 3\n").content,
                TextParagraph("\n\n\nTextField 1\nTextField 2\nTextField 3\n").content,
            ],
            run_spacing={"xs": 10},
        ),
    )
    page_resize(None)


ft.app(main)
#ft.app(target=main, view=ft.AppView.WEB_BROWSER)
