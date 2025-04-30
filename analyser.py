import psutil
import time
from datetime import datetime

def get_python_process():
    """Returns the 'main.py' process if it's running, otherwise returns None."""
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        if 'python' in process.info['name'].lower() and 'main.py' in process.info['cmdline']:
            return process
    return None

def log(message):
    """Function to log messages with timestamp."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

def track_resources(log_file=None):
    """Tracks the resource usage (CPU, Memory) of the 'main.py' process and logs it."""
    process = get_python_process()
    if not process:
        log("The 'main.py' process is not running.")
        return
    
    try:
        cpu_usage = process.cpu_percent(interval=1)
        memory_info = process.memory_info()
        memory_usage = memory_info.rss / (1024 * 1024)
        
        resource_info = f"'main.py' resource usage: CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage:.2f} MB"
        
        log(resource_info)
        
        if log_file:
            with open(log_file, 'a') as f:
                f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {resource_info}\n")
        
        if cpu_usage > 80:
            log("Warning: 'main.py' is consuming too much CPU!")
        
        if memory_usage > 500:
            log("Warning: 'main.py' is consuming too much memory!")
            
    except psutil.NoSuchProcess:
        log("The 'main.py' process was closed while monitoring.")
    except Exception as e:
        log(f"Error while monitoring the 'main.py' process: {e}")

def main():
    log("Starting resource monitoring for 'main.py'.")
    
    log_file = "resource_usage.log"
    
    while True:
        track_resources(log_file)
        time.sleep(5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("'main.py' resource monitoring stopped by user.")
