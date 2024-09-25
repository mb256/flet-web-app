import flet as ft


def main(page: ft.Page):
    page.title = "Design example"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 25
    page.window.width = 1200
    page.window.height = 800
    page.update()

    grid_view = ft.GridView(
        expand=1,
        runs_count=2,
        max_extent=500,
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
                width=300,
                height=200,
                border_radius=10,
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
                width=1100,
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
                width=1100,
                height=650,
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
                width=1100,
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
