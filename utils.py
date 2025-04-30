##Funções auxiliares
import psutil
from datetime import datetime

def is_lol_running():
    return any("LeagueClientUx.exe" in p.name() for p in psutil.process_iter())

def log(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")
