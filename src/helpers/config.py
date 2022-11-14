from pathlib import Path
import sys, json, os

def set(configFile):
    file = Path(configFile)

    if file.is_file():
        configData = getConfig(configFile)
        if configData['debug']:
        	print("Config file loaded")

        return configData

    return sys.exit(f"Config file not found: {configFile}")

def getConfig(configFile):
    with open(configFile) as file:
        data = file.read()

    return json.loads(data)

def get(key):
	configData = set('./config.json')
	if configData is None:
		return False
	return configData[key]