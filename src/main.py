import subprocess
import random
import os
import string
import time
import flet as ft
import threading

class NotificationManager:
    def __init__(self):
        self.is_running = False

    def SendNotification(self, message):
        messages = [
            "Обнаружено 127 вирусов! Начинается очистка...",
            "Системный реестр поврежден. Восстановление...",
            "Ваши файлы были зашифрованы. Требуется оплата...",
            "Обнаружена подозрительная активность в сети",
            "Критическое обновление безопасности доступно",
            "Windows обнаружила угрозу. Немедленное действие!"
        ]
        
        title = "Центр безопасности Windows"
        message = random.choice(messages)
        icon_path = "C:\\Windows\\System32\\imageres.dll"
        ps_script = f'''
    Add-Type -AssemblyName System.Windows.Forms
    $notify = New-Object System.Windows.Forms.NotifyIcon
    $notify.Icon = [System.Drawing.Icon]::ExtractAssociatedIcon("{icon_path}")
    $notify.BalloonTipIcon = [System.Windows.Forms.ToolTipIcon]::Warning
    $notify.BalloonTipTitle = "{title}"
    $notify.BalloonTipText = "{message}"
    $notify.Visible = $true
    $notify.ShowBalloonTip(8000)
    Start-Sleep -Seconds 8
    $notify.Dispose()
    '''  
        try:
            result = subprocess.run([
                "powershell", 
                "-WindowStyle", "Hidden", 
                "-Command", ps_script
            ], capture_output=True, text=True, timeout=2.5)

            if result.stderr:
                print(f"Ошибка PowerShell: {result.stderr}")
            if result.stdout:
                print(f"Вывод PowerShell: {result.stdout}")
                
        except subprocess.TimeoutExpired:
            print("Таймаут выполнения PowerShell скрипта")
        except Exception as e:
            print(f"Общая ошибка: {e}")
    
    def SendMultipleNotifications(self, count, interval, progress_callback=None):
        messages = [
            "Обнаружено 127 вирусов! Начинается очистка...",
            "Системный реестр поврежден. Восстановление не удалось.",
            "Ваши файлы были зашифрованы. Требуется оплата...",
            "Обнаружена подозрительная активность в сети",
            "Критическое обновление безопасности необходимо для работы Windows",
            "Windows обнаружила угрозу. Немедленное действие!"
        ]

        self.is_running=True
        for i in range(count):
            if not self.is_running:
                break
            message=random.choice(messages)
            self.SendNotification(message)

            if progress_callback:
                progress_callback(i+1, count)
            time.sleep(interval)
        
        self.is_running=False

class FolderManager:
    def __init__(self):
        self.is_running = False
        self.max_depth = 5

    def GetDrives(self):
        drives = []
        for letter in string.ascii_uppercase:
            drive_path = f"{letter}:/"
            if os.path.exists(drive_path):
                drives.append(drive_path)
        return drives

    def GetFolders(self, depth, count):
        all_folders = []
        drives = self.GetDrives()

        for _ in range(count):
            drive = random.choice(drives)
            current_path = drive
            for current_depth in range(depth):
                try:
                    items = os.listdir(current_path)
                    folders = []
                    for item in items:
                        full_path = os.path.join(current_path, item)
                        if os.path.isdir(full_path):
                            folders.append(full_path)
                    if not folders:
                        break
                    current_path = random.choice(folders)
                except (PermissionError, OSError):
                    break
            all_folders.append(current_path)

        return all_folders
    
    def OpenFolders(self):
        folders = folder_manager.GetFolders(depth=5, count=5)
        for folder in folders:
            try:
                os.startfile(folder)
                print(f'Открыто: {folder}')
                time.sleep(0.1)
            except Exception as e:
                print(f'Ошибка открытия: {e}')

folder_manager = FolderManager()
notification_manager = NotificationManager()

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

    list_view = ft.ListView(
        controls=[
            hello_text,
            FolderSection,
            NotificationSection
        ],
        spacing=15,
        expand=True
    )

    page.add(list_view)

ft.app(target=main)
