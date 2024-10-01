import flet as ft


def main(page: ft.Page):
    page.add(ft.Text(f"Initial route: {page.route}"))
    print(f"ROUTE: {page.route}")


ft.app(main, view=ft.AppView.WEB_BROWSER)
