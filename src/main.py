import subprocess
import random
import os
import string
import time
import flet as ft
import threading
import platform
import socket

from datetime import datetime
from managers.folder import FolderManager
from managers.notification import NotificationManager

notification_manager = NotificationManager()
folder_manager = FolderManager()

def main(page: ft.Page):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    page.fonts = {
            'SuperMorning': os.path.join(current_dir, 'assets', 'fonts', 'SuperMorning-ZpZwZ.ttf'),
            'HomeVideo': os.path.join(current_dir, 'assets', 'fonts', 'HomeVideo-BLG6G.ttf')
            }

    icon_path = os.path.join(current_dir, 'assets', 'icon.ico')
    page.window.icon = icon_path
    page.title = 'JOKER'
    page.window.width = 475
    page.window.height = 600
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 20
    page.window.resizable = False
    page.window.maximizable = False


    hello_text = ft.Text(
        value='Welcome to JOKER',
        size=42,
        color=ft.Colors.RED,
        text_align='center',
        font_family='HomeVideo'
    )

    # notifications gui

    notification_description = ft.Text(
        'Отправляет реалистичные уведомления Windows',
        size=14,
        color=ft.Colors.GREY,
        text_align='center'
    )

    count_field = ft.TextField(
        label='Количество уведомлений',
        keyboard_type=ft.KeyboardType.NUMBER,
        width=400
    )

    interval_field = ft.TextField(
        label='Интервал',
        keyboard_type=ft.KeyboardType.NUMBER,
        width=400
    )

    progress_bar = ft.ProgressBar(width=400, visible=False)
    progress_text = ft.Text('', size=12, color=ft.Colors.GREY)

    start_button = ft.ElevatedButton( #notifications
        'Начать отправку',
        width=400,
        icon=ft.Icons.PLAY_ARROW
    )

    stop_button = ft.ElevatedButton( #notifications
        'Остановить',
        width=400,
        icon=ft.Icons.STOP,
        visible=False
    )

    # folder gui

    folder_description = ft.Text(
        'Открывает указанное количество папок',
        size=14,
        color=ft.Colors.GREY,
        text_align='center'
    )

    folder_count_field = ft.TextField(
        label='Количество папок',
        keyboard_type=ft.KeyboardType.NUMBER,
        width=400
    )

    folder_depth_field = ft.TextField(
        label='Глубина пути',
        keyboard_type=ft.KeyboardType.NUMBER,
        width=400
    )

    folder_button = ft.ElevatedButton(
        text='Открыть папки',
        width=400,
        icon=ft.Icons.SEND
    )

    # system info gui

    system_info_description = ft.Text(
        'Информация системы и характеристики ПК',
        size=14,
        color=ft.Colors.GREY,
        text_align='center'
    )



    def UpdateProgressBar(current, total):
        progress_bar.value = current / total
        progress_text.value = f"Отправлено {current} из {total} уведомлений"
        page.update()

    def StartNotifying(e):
        try:
            count = int(count_field.value)
            interval = float(interval_field.value)

            if count <= 0 or interval <= 0:
                raise ValueError('Значения должны быть больше 0')
            
            start_button.visible = False
            stop_button.visible = True
            progress_bar.visible = True
            page.update()

            def run_notifications():
                notification_manager.SendMultipleNotifications(count, interval, UpdateProgressBar)
                start_button.visible = True
                stop_button.visible = False
                progress_bar.visible = False
                progress_text.value = 'Готово!'
                page.update()
            
            thread = threading.Thread(target=run_notifications)
            thread.daemon = True
            thread.start()

        except ValueError as e:
            progress_text.value = f'Ошибка:{str(e)}'
            page.update()

    def StopNotifying(e):
        notification_manager.is_running = False
        progress_text.value = 'Остановлено'
        page.update()

    def OpenFoldersButton(e):
        try:
            count = int(folder_count_field.value)
            depth = int(folder_depth_field.value)
            if count <= 0 or depth <= 0:
                    raise ValueError('Значения должны быть больше 0')
            folder_manager.OpenFolders(depth, count)
        except Exception as e:
            print(f'Ошибка {e}')

    folder_button.on_click = OpenFoldersButton
    start_button.on_click = StartNotifying
    stop_button.on_click = StopNotifying

    NotificationSection = ft.Column(
        controls=[
            # Notification Options
            ft.Text("🔔 Уведомления", size=20, weight="bold"),
            notification_description,
            ft.Divider(),
            count_field,
            interval_field,
            start_button,
            stop_button,
            progress_bar,
            progress_text,
        ],
        spacing=15,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    FolderSection = ft.Column(
        controls=[
            # Folder Options
            ft.Text("📂 Управление папками", size=20, weight="bold"),
            folder_description,
            ft.Divider(),
            folder_count_field,
            folder_depth_field,
            folder_button,
        ],
        spacing=15,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    SystemInfoSection = ft.Column(
        controls = [
            #System Info Collecting
            ft.Text("💿 Информация о системе", size=20, weight="bold"),
            system_info_description,
            ft.Divider(),
            ft.Text(f'''
        Операционная система: {platform.system()},
        Версия ОС: {platform.version()},
        Архитектура: {platform.architecture()[0]},
        Имя компьютера: {socket.gethostname()},
        Имя пользователя: {os.getlogin()},
        Процессор: {platform.processor()},
        Количество ядер: {os.cpu_count()},
        Время запуска: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
        Рабочая папка: {os.getcwd()}
                    ''', size = 15, weight='bold', color='grey'),
        ],
        spacing=15,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    list_view = ft.ListView(
        controls=[
            hello_text,
            SystemInfoSection,
            FolderSection,
            NotificationSection
        ],
        spacing=15,
        expand=True
    )

    page.add(list_view)

ft.app(target=main)
