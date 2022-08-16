import configparser
from pathlib import Path
import os

CONFIG_FILE = Path(os.path.abspath('application/home/common/appconfig.ini'))
APPCONFIG = configparser.ConfigParser()
APPCONFIG.read(CONFIG_FILE)
