import flet as ft


def menu_action(item):
    print(f"Menu option clicked!  {item.name} ???")


def main(page: ft.Page):
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    pb = ft.PopupMenuButton(icon=ft.icons.MENU_ROUNDED,
        items=[
            ft.PopupMenuItem(icon=ft.icons.LABEL_IMPORTANT_OUTLINE_SHARP, text="option 1", on_click=menu_action),
            ft.PopupMenuItem(icon=ft.icons.LABEL_IMPORTANT_OUTLINE_SHARP, text="option 2", on_click=menu_action),
            ft.PopupMenuItem(icon=ft.icons.LABEL_IMPORTANT_OUTLINE_SHARP, text="option 3", on_click=menu_action),
            ft.PopupMenuItem(icon=ft.icons.LABEL_IMPORTANT_OUTLINE_SHARP, text="option 4", on_click=menu_action),
            ft.PopupMenuItem(icon=ft.icons.LABEL_IMPORTANT_OUTLINE_SHARP, text="option 5", on_click=menu_action),
            ft.PopupMenuItem(
                content=ft.Row(
                    [
                        ft.Icon(ft.icons.HOURGLASS_TOP_OUTLINED),
                        ft.Text("Item with a custom content"),
                    ]
                ),
                on_click=lambda _: print("Button with a custom content clicked!"),
            ),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(
                text="Checked item", checked=False, on_click=check_item_clicked
            ),
        ]
    )
    page.add(pb)


ft.app(main)
