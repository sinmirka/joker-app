import platform
import os
import socket
from datetime import datetime

def get_system_info():
    """Собирает основную информацию об устройстве"""
    print("🖥️ Сбор информации об устройстве...")
    
    info = {
        "Операционная система": platform.system(),
        "Версия ОС": platform.version(),
        "Архитектура": platform.architecture()[0],
        "Имя компьютера": socket.gethostname(),
        "Имя пользователя": os.getlogin(),
        "Процессор": platform.processor(),
        "Количество ядер": os.cpu_count(),
        "Время запуска": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Рабочая папка": os.getcwd()
    }
    
    print("✅ Информация собрана:")
    for key, value in info.items():
        print(f"   {key}: {value}")
    
    return info

get_system_info()