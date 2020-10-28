import subprocess
import time
import os, signal

while True:
    print("update bot")
    PIPE = subprocess.PIPE
    p = subprocess.Popen("python main.py", shell = True)
    time.sleep(60)
    subprocess.Popen.kill(p)
