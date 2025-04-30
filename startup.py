import os
import winreg

APP_NAME = "LoL-Accept-Py"
REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"

def add_to_startup():
    exe_path = os.path.abspath("main.pyw")
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, APP_NAME, 0, winreg.REG_SZ, f'python "{exe_path}"')
    winreg.CloseKey(key)

def remove_from_startup():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(key, APP_NAME)
        winreg.CloseKey(key)
    except FileNotFoundError:
        pass
