import configparser
from pathlib import Path
import os

CONFIG_FILE = os.path.join(
	os.path.dirname(
		os.path.realpath(__file__)
		),
		'appconfig.ini'
	)
APPCONFIG = configparser.ConfigParser()
APPCONFIG.read(CONFIG_FILE)

STATIC_DIR = os.path.join(
	os.path.dirname(
		os.path.realpath(__file__)
	),
	'..', 
	'static'
)
