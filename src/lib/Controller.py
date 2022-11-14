import sys, os, json
import platform
from pathlib import Path
import glob
from src.lib.Command import Command
from src.helpers import *
from src.commands import *
from pprint import pprint

class Controller:

    def __init__(self, args, options=None):
        self.args = self.formatArgs(args)
        self.options = self.setOptions(options)

        console.print('App starting...')

        self.commands = []
        self.isRunning = False

    def run(self):
        console.clear()

        self.displayStats()

        self.loadCommands('src/commands/*.py')

        self.isRunning = True

        while self.isRunning:
            console.clear()
            print(f"CLI Tool {config.get('name')} | Commands\n\n")
            self.listCommands()
            self.getInput()

            if input("\n\nPress Enter to continue..."):
                self.isRunning = False


    def getInput(self):
        command = input('>> ')
        return self.executeCommand(self.commands[int(command)])

    def executeCommand(self, command):
        obj = self.getCommandObj(command)
        print("\n\n")
        try:
            if obj.__getattribute__('handle'):
                obj.handle()
        except:
            pass

        return obj

    def loadCommands(self, path):
        files = glob.glob(path)
        if len(files) < 1: return

        for file in files:
            file = os.path.basename(file)[:-3]
            if file not in config.get('commandBlacklist'):
                try:
                    obj = self.getCommandObj(file)
                    self.commands.append(file)
                    console.print(f"Command {file} has been loaded")
                except:
                    console.print(f"Command {file} has failed loading...")

    def listCommands(self):
        if len(self.commands) < 1: return sys.exit(f"Failed loading any commands")
        for i in range(0, len(self.commands)):
            print("\n\n")
            print(f"[{i}] {self.commands[i]}")
        print("\n\n")


    def getCommandObj(self, command) -> Command:
        try:
            module = globals()[command]
            obj = module.__getattribute__(command)()
            return obj
        except:
            console.print(f"Command {file} has failed initializing...")


    def displayStats(self):
        for x in self.getStats():
            console.print(f"{x['name']}: {x['value']}")

    def getStats(self):
        stats = [
            {
            'name': "Python version",
            'value': platform.python_version()
            },
        ]

        return stats

    def formatArgs(self, args):
        return args

    def setOptions(self, options):
        return options

