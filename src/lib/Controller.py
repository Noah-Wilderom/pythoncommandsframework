import sys, os
import platform
from pathlib import Path
from src.helpers import *


class Controller:

    def __init__(self, args, options=None):
        self.args = self.formatArgs(args)
        self.options = self.setOptions(options)
        print('App starting...')


    def displayStats(self):
        for x in self.getStats():
            print(f"{x['name']}: {x['value']}")

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
            print('Config file loaded')
            return True

        # print(f"Config file not found: {self.options['configFile']}")
        return sys.exit(f"Config file not found: {self.options['configFile']}")

    def run(self):
        console.clear()

        self.setConfig()

        self.displayStats()


    def formatArgs(self, args):
        return args

    def setOptions(self, options):
        return options
