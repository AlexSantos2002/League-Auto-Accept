
# 🎮 League Auto-Accept

Automatically accepts queue matches in **League of Legends** using the LCU API.

## 🧠 About

This lightweight Python tool checks the current **game phase** using the local client API and instantly accepts matches when they pop up (ReadyCheck phase). Ideal for multitasking or AFK moments while waiting for queue.

## ✨ Features

- ✅ Automatically accepts match queue pop-ups.
- 🕵️ Detects when the League client is running.
- 🔄 Lightweight background process (optionally starts with Windows).
- 🖥️ GUI in future versions.
- 🔒 No cheats or injection – purely reads Riot's official client API.

---

## 🚀 How It Works

It connects to the League of Legends **LCU API** via local HTTPS using:
- App port
- Authentication token

These values are extracted directly from the `LeagueClientUx.exe` process command line.

---

## 🛠️ Installation

1. **Install Python 3.8+**  
   https://www.python.org/downloads/

2. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/League-Auto-Accept
   cd League-Auto-Accept
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Script**
   ```bash
   python main.py
   ```

---

## 📦 Requirements:

- Python 3.8+
- League of Legends (client must be open)
- Packages:
  - psutil
  - requests

Install if needed:
```bash
pip install psutil requests
```

---

## ⚙️ Optional: Auto Start on Windows

The project includes a registry helper to **add/remove the script to Windows startup**.

Use the following Python functions to add or remove the script from startup:

```python
from startup import add_to_startup, remove_from_startup

# Adds to autostart
add_to_startup()

# Removes from autostart
remove_from_startup()
```

---

## 🛡️ Disclaimer

This tool uses only **publicly exposed client APIs**. It does **not interact with Riot's servers**, game memory, or inject anything.  
Use at your own risk. This is a personal automation tool, and **no warranty is provided.**
