import string
import os
import time
import random

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
    
    def OpenFolders(self, depth, count):
        folders = self.GetFolders(depth, count)
        for folder in folders:
            try:
                os.startfile(folder)
                print(f'Открыто: {folder}')
                time.sleep(0.1)
            except Exception as e:
                print(f'Ошибка открытия: {e}')