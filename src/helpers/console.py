
import sys, os
from sys import platform


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
