import flet as ft


def main(page: ft.Page):
    page.add(ft.SafeArea(ft.Text("\nHello, Flet!\n")))
    page.add(ft.SafeArea(ft.Text("An example Flet based page\n")))
    page.add(ft.SafeArea(ft.Text("Use for experiments")))


ft.app(main)
