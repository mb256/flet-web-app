import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors


def main(page: Page):
    page.title = "Routes Example"

    print("Initial route:", page.route)

    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Flet app")),
                    ElevatedButton("Go to settings", on_click=open_settings),
                    ElevatedButton("Go to my page", on_click=open_my_page),
                ],
            )
        )
        if page.route == "/settings" or page.route == "/settings/mail":
            page.views.append(
                View(
                    "/settings",
                    [
                        AppBar(title=Text("Settings"), bgcolor=colors.SURFACE_VARIANT),
                        Text("Settings!", style="bodyMedium"),
                        ElevatedButton(
                            "Go to mail settings", on_click=open_mail_settings
                        ),
                    ],
                )
            )
        if page.route == "/settings/mail":
            page.views.append(
                View(
                    "/settings/mail",
                    [
                        AppBar(
                            title=Text("Mail Settings"), bgcolor=colors.SURFACE_VARIANT
                        ),
                        Text("Mail settings!"),
                    ],
                )
            )
        if page.route == "/my_page":
            page.views.append(
                View(
                    "/my_page",
                    [
                        AppBar(title=Text("My page"), bgcolor=colors.SURFACE_VARIANT),
                        Text("Welcome to my page!", size=36, color=colors.PINK_200),
                        ElevatedButton("Go to seznam.cz", on_click=open_seznam),
                    ]
                )
            )
        page.update()

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    def open_mail_settings(e):
        page.go("/settings/mail")

    def open_settings(e):
        page.go("/settings")

    def open_my_page(e):
        page.go("/my_page")

    def open_seznam(e):
        page.launch_url('https://seznam.cz')

    page.go(page.route)


flet.app(target=main, view=flet.AppView.WEB_BROWSER)
