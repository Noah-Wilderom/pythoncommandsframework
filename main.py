#!/usr/bin/python

import sys, os
from src.lib.Controller import Controller

settings = {
	"debug": True,
	"cache": False,
	"configFile": "./config.py"
}

def main(*, args, options=None):
	obj = Controller(args, options)

	obj.run()


main(args=sys.argv, options=settings) if __name__ == '__main__' else os.exit("Please start the 'main.py' file")
