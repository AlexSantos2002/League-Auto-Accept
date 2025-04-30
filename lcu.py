import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_phase(auth_url):
    try:
        url = f"{auth_url}/lol-gameflow/v1/gameflow-phase"
        response = requests.get(url, verify=False)
        return response.text.strip('"')
    except:
        return "Unknown"

def accept_match(auth_url):
    try:
        url = f"{auth_url}/lol-matchmaking/v1/ready-check/accept"
        requests.post(url, verify=False)
    except:
        pass
