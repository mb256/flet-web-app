import flet as ft


def main(page: ft.Page):
    page.title = "Design example"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 25
    page.update()

    grid_view = ft.GridView(
        expand=1,
        runs_count=2,
        max_extent=100,
        child_aspect_ratio=1.0,
        spacing=2,
        run_spacing=2,
    )

    for i in range(0, 90):
        grid_view.controls.append(
            ft.Container(
                content=ft.Text(f"* {i} *"),
                margin=2,
                padding=2,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.GREY_700,
                width=80,
                height=40,
                border_radius=10,
            )
        )

    my_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("The Enchanted Nightingale"),
                            subtitle=ft.Text(
                                "Music by Julie Gable. Lyrics by Sidney Stein."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )

    row = ft.Column(
        [
            ft.Container(
                content=ft.Text("Row A Row A Row A Row A Row A"),
                margin=1,
                padding=1,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                width=400,
                height=30,
                border_radius=30,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=4,
                    color=ft.colors.BLUE_GREY_300,
                    offset=ft.Offset(0, 0),
                    blur_style=ft.ShadowBlurStyle.OUTER,
                )
            ),

            ft.Container(
                content=grid_view,
                margin=1,
                padding=1,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                width=400,
                height=400,
                border_radius=30,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=4,
                    color=ft.colors.BLUE_GREY_300,
                    offset=ft.Offset(0, 0),
                    blur_style=ft.ShadowBlurStyle.OUTER,
                )
            ),

            ft.Container(
                content=ft.Text("Row B Row B Row B Row B Row B"),
                margin=1,
                padding=1,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK12,
                width=400,
                height=30,
                border_radius=30,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=4,
                    color=ft.colors.BLUE_GREY_300,
                    offset=ft.Offset(0, 0),
                    blur_style=ft.ShadowBlurStyle.OUTER,
                )
            ),
        ]
    )

    page.add(row)
    page.update()


ft.app(target=main)
