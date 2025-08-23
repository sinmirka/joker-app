import subprocess
import random
import os
import flet as ft

def powershell_notification():
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
        ], capture_output=True, text=True, timeout=10)

        if result.stderr:
            print(f"Ошибка PowerShell: {result.stderr}")
        if result.stdout:
            print(f"Вывод PowerShell: {result.stdout}")
            
    except subprocess.TimeoutExpired:
        print("Таймаут выполнения PowerShell скрипта")
    except Exception as e:
        print(f"Общая ошибка: {e}")

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
        value='JOKER - Программа для пранков',
        size=20,
        color='blue',
        weight='bold',
        text_align='center'
    )

    def NotifyClicked(e):
        powershell_notification()

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