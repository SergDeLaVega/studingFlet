import flet as ft


def main(page: ft.Page):
    page.title = "Погодная программа"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text('Какой то текст'),
                
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)