import sys, os
from src.helpers import *


class Controller:

    def __init__(self, args, options=None):
        self.args = self.formatArgs(args)
        self.options = self.setOptions(options)
        print('App starting...')

    def run(self):
        console.clear()

        print('App started...')

    def formatArgs(self, args):
        return args

    def setOptions(self, options):
        return options
