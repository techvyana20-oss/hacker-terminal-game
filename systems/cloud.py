import os
from config import SAVE_FILE, CLOUD_FILE

def cloud_save():
    if os.path.exists(SAVE_FILE):
        data = open(SAVE_FILE).read()
        open(CLOUD_FILE, "w").write(data)
