import sys, os, json
import platform
from pathlib import Path
from src.helpers import *


class Controller:

    def __init__(self, args, options=None):
        self.args = self.formatArgs(args)
        self.options = self.setOptions(options)
        self.setConfig()

        self.print('App starting...')

    def run(self):
        console.clear()

        self.displayStats()

        self.loadCommands()



    def displayStats(self):
        for x in self.getStats():
            self.print(f"{x['name']}: {x['value']}")

    def getStats(self):
        stats = [
            {
            'name': "Python version",
            'value': platform.python_version()
            },
        ]

        return stats

    def setConfig(self):
        file = Path(self.options['configFile'])

        if file.is_file():
            self.configData = self.getConfig()
            self.print('Config file loaded')

            return True

        # print(f"Config file not found: {self.options['configFile']}")
        return sys.exit(f"Config file not found: {self.options['configFile']}")

    def formatArgs(self, args):
        return args

    def setOptions(self, options):
        return options

    def print(self, *args):
        if self.config('debug'):
            for x in args:
                print(x)
        pass

    def getConfig(self):
        with open(self.options['configFile']) as file:
            data = file.read()

        return json.loads(data)

    def config(self, key):
        if self.configData is None:
            return False

        return self.configData[key]