import time
from cmdline import get_command_line
from lcu import get_phase, accept_match
from utils import is_lol_running, log

def get_valid_auth():
    if not is_lol_running():
        return {"auth_url": "", "token": "", "port": ""}
    return get_command_line()

def main():
    log("Iniciando Auto-Accept do LoL. Pressione Ctrl+C para parar.")
    auth = get_valid_auth()

    while True:
        if not is_lol_running():
            log("Cliente do LoL não está em execução. Aguardando...")
            time.sleep(5)
            continue

        if not auth["auth_url"]:
            auth = get_valid_auth()
            time.sleep(1)
            continue

        phase = get_phase(auth["auth_url"])
        log(f"Fase atual: {phase}")

        if phase == "ReadyCheck":
            log("Partida encontrada! Aceitando...")
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
        log("Auto-Accept encerrado pelo usuário.")
