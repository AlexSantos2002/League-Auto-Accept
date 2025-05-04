# League Auto-Accept

Automatically accepts queue matches in **League of Legends** using the LCU API.

## About

This lightweight Python tool checks the current **game phase** using the local client API and instantly accepts matches when they appear (ReadyCheck phase). Ideal for multitasking or being away from the PC while waiting in queue.

## Features

- Automatically accepts match queue pop-ups
- Detects when the League client is running
- Lightweight background process (optionally starts with Windows)
- No cheats or injection – strictly reads Riot's official client API

## How It Works

It connects to the League of Legends **LCU API** via local HTTPS using:
- Application port
- Authentication token

These values are extracted directly from the `LeagueClientUx.exe` process command line.

## Installation

1. **Install Python 3.8 or newer**  
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

4. **Run the script**
   ```bash
   python main.py
   ```

## Requirements

- Python 3.8 or newer
- League of Legends (client must be open)
- Packages:
  - psutil
  - requests

Install if needed:
```bash
pip install psutil requests
```

## Optional: Auto Start on Windows

The project includes a registry helper to **add or remove the script to Windows startup**.

Use the following Python functions:

```python
from startup import add_to_startup, remove_from_startup

# Add to startup
add_to_startup()

# Remove from startup
remove_from_startup()
```