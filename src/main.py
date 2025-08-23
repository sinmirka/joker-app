import subprocess
import random
import os
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
            ], capture_output=True, text=True, timeout=3)

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
            "Системный реестр поврежден. Восстановление...",
            "Ваши файлы были зашифрованы. Требуется оплата...",
            "Обнаружена подозрительная активность в сети",
            "Критическое обновление безопасности доступно",
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

def main(page: ft.Page):
    icon_path = 'assets/icon.png'

    if os.path.exists(icon_path):
        page.window.icon = icon_path
    page.title = 'JOKER'
    page.window.width = 450
    page.window.height = 650
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 20

    notification_manager = NotificationManager()

    hello_text = ft.Text(
        value='🎭 JOKER - Программа для пранков',
        size=24,
        color=ft.Colors.BLUE,
        weight='bold',
        text_align='center'
    )

    description = ft.Text(
        'Отправляет реалистичные уведомления Windows',
        size=14,
        color=ft.Colors.GREY,
        text_align='center'
    )

    count_field = ft.TextField(
        label='Количество уведомлений',
        keyboard_type=ft.KeyboardType.NUMBER,
        value='5',
        width=400
    )

    interval_field = ft.TextField(
        label='Интервал',
        keyboard_type=ft.KeyboardType.NUMBER,
        width=400,
        value="3"
    )

    progress_bar = ft.ProgressBar(width=400, visible=False)
    progress_text = ft.Text('', size=12, color=ft.Colors.GREY)

    start_button = ft.ElevatedButton(
        'Начать отправку',
        width=400,
        icon=ft.Icons.PLAY_ARROW
    )

    stop_button = ft.ElevatedButton(
        'Остановить',
        width=400,
        icon=ft.Icons.STOP,
        visible=False
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

    column = ft.Column(
        controls=[
            hello_text,
            description,
            ft.Divider(),
            count_field,
            interval_field,
            start_button,
            stop_button,
            progress_bar,
            progress_text
        ],
        spacing=15,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(column)

ft.app(target=main)