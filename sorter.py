from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import zipfile
import shutil
import time
import os


class MYSorter:
    Data_path = None
    Sorted_path = None
    Backup = None
    Backup_path = None


    @staticmethod
    def loadSettings(data_path: str, sorted_path: str, backup: bool, backup_path: str) -> dict:
        global Data_path, Sorted_path, Backup, Backup_path

        try:
            Data_path = data_path
            if not os.path.exists(Data_path):
                print(f"Error loading settings: Data path '{Data_path}' does not exist.")
                return {"data": None, "status": "error", "message": f"Data path '{Data_path}' does not exist.", "code": 400}

            Sorted_path = sorted_path
            if not os.path.exists(Sorted_path):
                os.makedirs(Sorted_path)

            Backup = backup
            Backup_path = backup_path
            if Backup and not os.path.exists(Backup_path):
                os.makedirs(Backup_path)

            print(f"Settings loaded: Data_path={Data_path}, Sorted_path={Sorted_path}, Backup={Backup}, Backup_path={Backup_path}")
            return {"data": { "Data_path": Data_path, "Sorted_path": Sorted_path, "Backup": Backup, "Backup_path": Backup_path}, "status": "success", "message": "Settings loaded successfully.", "code": 200}
        except Exception as e:
            print(f"Error loading settings: {e}")
            return {"data": None, "status": "error", "message": str(e), "code": 500}

    @staticmethod
    def teszt():
        global Data_path, Sorted_path, Backup, Backup_path
        print(Data_path, Sorted_path, Backup, Backup_path)

    @staticmethod
    def SortFiles():
        try:
            print("Files sorted successfully.")
        except Exception as e:
            print(f"Error sorting files: {e}")

    @staticmethod
    def ZipFiles():
        try:
            print("Files zipped successfully.")
        except Exception as e:
            print(f"Error zipping files: {e}")



MYSorter.loadSettings(data_path = "./data", sorted_path = "./sorted", backup = True, backup_path = "./backup")
#MYSorter.teszt()
MYSorter.SortFiles()
#MYSorter.ZipFiles()