import flet as ft


def main(page: ft.Page):
    page.scroll = "auto"  # Povolení scrollování stránky

    def scroll_to(e):
        # Získáme cíl scrollování z data atributu tlačítka
        target = page.get_control(e.control.data)
        # Nascrollujeme na daný element
        target.scroll_into_view()
        page.update()

    # Vytvoření navigačních tlačítek
    nav_buttons = ft.Row(
        controls=[
            ft.ElevatedButton(
                text="Sekce 1",
                data="section1",  # ID sekce pro scroll
                on_click=scroll_to
            ),
            ft.ElevatedButton(
                text="Sekce 2",
                data="section2",
                on_click=scroll_to
            ),
            ft.ElevatedButton(
                text="Sekce 3",
                data="section3",
                on_click=scroll_to
            ),
        ],
        spacing=10
    )

    # Vytvoření obsahu sekcí
    content = ft.Column([
        nav_buttons,

        # Sekce 1
        ft.Container(
            content=ft.Column([
                ft.Text("Sekce 1", size=30, weight="bold"),
                ft.Text("Obsah první sekce...", size=16),
                ft.Container(height=300, bgcolor=ft.colors.BLUE_100)
            ]),
            key="section1"  # ID pro scrollování
        ),

        # Sekce 2
        ft.Container(
            content=ft.Column([
                ft.Text("Sekce 2", size=30, weight="bold"),
                ft.Text("Obsah druhé sekce...", size=16),
                ft.Container(height=300, bgcolor=ft.colors.GREEN_100)
            ]),
            key="section2"
        ),

        # Sekce 3
        ft.Container(
            content=ft.Column([
                ft.Text("Sekce 3", size=30, weight="bold"),
                ft.Text("Obsah třetí sekce...", size=16),
                ft.Container(height=300, bgcolor=ft.colors.RED_100)
            ]),
            key="section3"
        ),
    ])

    # Přidání obsahu na stránku
    page.add(content)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)