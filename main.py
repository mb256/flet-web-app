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
            padding=1,
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


class ProjectParagraph(ft.Column):
    def __init__(self, page: ft.Page, headline, text, picture, to_key=None):
        super().__init__()

        self.headline = ft.Text(value=headline, size=22, col={"md": 6}, text_align=ft.TextAlign.CENTER)
        self.text_with_picture = ft.Row(
            [
                ft.Text(value=text, size=16, col={"md": 6}, expand=True),
                ft.Text(value="PICTURE PLACEHOLDER", size=10, col={"md": 6}, expand=True),
                # None
            ]
        )

        def go_to_top(e):
            page.scroll_to(key="to_top")

        self.project_link = ft.Container(
            ft.TextButton(text="go to github", on_click=go_to_top,
                          style=ft.ButtonStyle(color=ft.colors.WHITE)),
            padding=5,
            col={"sm": 6, "md": 4, "xl": 2},
        )

        self.controls = [
            self.headline,
            self.text_with_picture,
            self.project_link
        ]

        self.col = {"md": 6}
        self.expand = True
        self.width = 200
        self.height = 400
        self.key = to_key


class TextParagraph:
    def __init__(self, text_par, to_key=None):
        self.content = ft.Container(
            ft.Text(value=text_par, size=22, col={"md": 6}, text_align=ft.TextAlign.CENTER,
                    expand=True, width=200, height=400, key=to_key),
            # alignment=ft.alignment.center,
            col={"md": 6},
        )


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK

    def go_to_contact(e):
        page.scroll_to(key="to_contact")
        # page.launch_url("https://google.com")

    def go_to_top(e):
        page.scroll_to(key="to_top")

    def open_google(e):
        page.launch_url("https://google.com")

    def open_seznam(e):
        page.launch_url("https://seznam.cz")

    def open_root(e):
        page.launch_url("https://root.cz")

    class MyTextButton:

        def __init__(self, btn_text: str, function, to_key=None):
            self.link_button_container = ft.Container(
                ft.TextButton(text=btn_text, on_click=function,
                              style=ft.ButtonStyle(color=ft.colors.WHITE),
                              key=to_key),
                padding=3,
                col={"sm": 6, "md": 4, "xl": 2},
            )

    class TextParagraphWithButton:
        def __init__(self, text_par: str, go_function=None, key_dest=None):
            to_top = MyTextButton("Back to Top", go_function).link_button_container

            self.content = ft.Column(
                [
                    ft.Container(
                        ft.Text(value=text_par, size=22, col={"md": 6}, text_align=ft.TextAlign.CENTER,
                                expand=True, key=key_dest),
                        # alignment=ft.alignment.center,
                        col={"md": 6},
                        padding=2,
                        margin=2,
                    ),
                    to_top,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )

    # def page_resize(e):
    #     pw.value = f"{page.width} px"
    #     pw.update()

    pw = ft.Text(bottom=50, right=50, style="displaySmall")
    page.overlay.append(pw)

    #page.on_resize = page_resize

    page.scroll = True
    page.theme_mode = ft.ThemeMode.DARK

    # Dynamic text on background
    background_image = DynamicTextOnBackground(messages, "/family_dark_dark_edge_1.jpg")
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
                MyTextButton("Contact", go_to_contact, to_key="to_top").link_button_container,
                MyTextButton("LinkedIn", open_google).link_button_container,
                MyTextButton("Micro projects", open_google).link_button_container,
                MyTextButton("Blog", open_google).link_button_container,
            ],
        ),
        ft.ResponsiveRow(
            [
                main_info.content,
                background_image.content,

                #TextParagraph("\n\n\nBlog article 1\n\nBlog article 2\n\nBlog article 3\n").content,
                #TextParagraph("\n\n\nMicro project 1\n\nMicro project 2\n\nMicro project 3\n").content,
                ProjectParagraph(page, "Mini Project 1", "Description of project number one", None),
                ProjectParagraph(page, "Mini Project 2", "Description of project number one", None),
                ProjectParagraph(page, "Mini Project 3", "Description of project number one", None),
                ProjectParagraph(page, "Mini Project 4", "Description of project number one", None),
                ProjectParagraph(page, "Mini Project 5", "Description of project number one", None),

                TextParagraphWithButton(text_par="\n\n\nContact\n\nemail: mb256@seznam.cz\n\n", go_function=go_to_top, key_dest="to_contact").content,
            ],
            run_spacing={"xs": 10},
        ),
    )
    #page_resize(None)


#ft.app(main)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
