#!/usr/bin/python

import sys, os
from src.lib.Controller import Controller

settings = {
	"configFile": "./config.json"
}

def main(*, args, options=None):
	obj = Controller(args, options)

	obj.run()


main(args=sys.argv, options=settings) if __name__ == '__main__' else sys.exit("Please start the 'main.py' file")
