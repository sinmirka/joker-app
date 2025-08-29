import subprocess
import os
import random
import time

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