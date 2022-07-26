import configparser

CONFIG_FILE = 'appconfig.ini'

APPCONFIG = configparser.ConfigParser()
APPCONFIG.read(CONFIG_FILE)
