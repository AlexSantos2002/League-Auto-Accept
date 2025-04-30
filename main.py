import time
from cmdline import get_command_line
from lcu import get_phase, accept_match

def main():
    print("Iniciando Auto-Accept do LoL. Pressione Ctrl+C para parar.")
    auth = get_command_line()

    while True:
        if not auth["auth_url"]:
            print("Esperando cliente do LoL iniciar...")
            time.sleep(5)
            auth = get_command_line()
            continue

        phase = get_phase(auth["auth_url"])
        print(f"Fase atual: {phase}")

        if phase == "ReadyCheck":
            print("Aceitando partida!")
            accept_match(auth["auth_url"])
            time.sleep(1)
        elif phase in ["Lobby", "Matchmaking"]:
            time.sleep(1)
        else:
            time.sleep(5)

if __name__ == "__main__":
    main()
