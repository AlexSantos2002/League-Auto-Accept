import subprocess
import re

def get_command_line():
    try:
        output = subprocess.check_output(
            ["powershell", "-Command",
             "Get-CimInstance Win32_Process -Filter \"name='LeagueClientUx.exe'\" | Select-Object -ExpandProperty CommandLine"],
            stderr=subprocess.DEVNULL,
            text=True
        )

        port = re.search(r'--app-port=(\d+)', output)
        token = re.search(r'--remoting-auth-token=([^\s"]+)', output)

        if port and token:
            return {
                "port": port.group(1),
                "token": token.group(1),
                "auth_url": f"https://riot:{token.group(1)}@127.0.0.1:{port.group(1)}"
            }
    except Exception as e:
        print("Erro ao obter dados do processo:", e)

    return {"auth_url": "", "token": "", "port": ""}
