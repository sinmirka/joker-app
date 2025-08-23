import flet as ft
import os

def main(page: ft.Page):
    icon_path = 'assets/icon.png'

    if os.path.exists(icon_path):
        page.window.icon = icon_path
    page.title = 'JOKER'
    page.window.width = 400
    page.window.height = 500
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    hello_text = ft.Text(
        value='JOKER - Пранкер',
        size=20,
        color='blue',
        weight='bold',
        text_align='center'
    )

    def NotifyClicked(e):
        print('Нажато')

    NotifyButton = ft.ElevatedButton(
        'Отправить уведомление от Windows',
        on_click=NotifyClicked,
        width=400
    )

    column = ft.Column(
        controls=[hello_text, NotifyButton],
        alignment=ft.MainAxisAlignment.CENTER
    )
    page.add(column)

ft.app(target=main)