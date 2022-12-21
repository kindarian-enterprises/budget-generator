from mongoengine import connect, disconnect
from uuid import uuid4
from flask_mongoengine import MongoEngine

def get_db_connection(alias=None):
    """
    Gets the DB connection
    """

    db_url = get_mongo_url()

    if alias is None:
        return connect(host=db_url)

    return connect(alias=alias, host=db_url)


def get_mongo_url():
    #code to get config from file and/or env vars
    #TODO this can't stay hardcoded....

    return f'mongodb://dbuser:somepassword@budget-generator-mongo:27017/budget-generator'
