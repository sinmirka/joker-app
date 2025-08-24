import flet as ft
import os

def main(page: ft.Page):
    # Получаем правильный путь к шрифту
    current_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(current_dir, "src", "assets", "fonts", "SuperPeanut-PVAK7.ttf")
    
    # Проверяем существование файла
    if os.path.exists(font_path):
        print(f"Файл шрифта найден: {font_path}")
        page.fonts = {'SuperPeanut': font_path}
        
        hello_text = ft.Text(
            value='Welcome to JOKER',
            size=24,
            color=ft.Colors.RED,
            weight='normal',
            text_align='center',
            font_family='SuperPeanut'
        )
        
        page.add(hello_text)
    else:
        print(f"Файл шрифта НЕ найден: {font_path}")
        # Покажем сообщение об ошибке
        page.add(ft.Text("Ошибка: файл шрифта не найден", color=ft.Colors.RED))

ft.app(target=main)