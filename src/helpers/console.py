
import sys, os
from sys import platform
from src.helpers import config
def getOs():
    if platform == "linux" or platform == "linux2":
        # linux
        return "linux"
    elif platform == "darwin":
        # OS X
        return "apple"
    elif platform == "win32":
        # Windows...
        return "windows"

    return False


def clear():
    device_os = getOs()
    if device_os == 'linux':
        os.system('clear')
    else:
        os.system('cls')

def print(self, *args):
    if config.get('debug'):
        for x in args:
            print(x)
    pass