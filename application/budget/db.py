from mongoengine import connect
from uuid import uuid4
# from flask_mongoengine import MongoEngine
from application.budget.common.config import APPCONFIG

def get_db_connection(alias: str=None):
    """
    Gets the DB connection
    """

    db_url = get_mongo_url()

    if alias is None:
        return connect(host=db_url)

    return connect(alias=alias, host=db_url)


def get_mongo_url() -> str:
    '''Funtion that gets mongo config from file and returns
       it as a string.'''
    db_user = APPCONFIG['database_config']['DBUSER']
    db_password = APPCONFIG['database_config']['DBPASSWORD']
    db_name = APPCONFIG['database_config']['DBNAME']
    db_host = APPCONFIG['database_config']['HOSTNAME']
    db_ports = APPCONFIG['database_config']['PORTS']

    return f'mongodb://{db_user}:{db_password}@{db_host}:{db_ports}/{db_name}'
