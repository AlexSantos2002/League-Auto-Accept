import time
from cmdline import get_command_line
from lcu import get_phase, accept_match
from utils import is_lol_running, log

def get_valid_auth():
    if not is_lol_running():
        return {"auth_url": "", "token": "", "port": ""}
    return get_command_line()

def main():
    log("Starting LoL Auto-Accept. Press Ctrl+C to stop.")
    auth = get_valid_auth()

    while True:
        if not is_lol_running():
            log("LoL client is not running. Waiting...")
            time.sleep(5)
            continue

        if not auth["auth_url"]:
            auth = get_valid_auth()
            time.sleep(1)
            continue

        phase = get_phase(auth["auth_url"])
        log(f"Current phase: {phase}")

        if phase == "ReadyCheck":
            log("Match found! Accepting...")
            accept_match(auth["auth_url"])
            time.sleep(1)
        elif phase in ["Lobby", "Matchmaking"]:
            time.sleep(1)
        else:
            time.sleep(5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("Auto-Accept stopped by user.")
