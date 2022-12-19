from mongoengine import connect



def get_db_connection():
    """
    Gets the DB connection
    """

    db_config = get_mongo_config()

    return connect(
        db_config['db_name'],
        **db_config['config']
    )


def get_mongo_config():
    #code to get config from file and/or env vars
    #TODO this can't stay hardcoded....

    return {
        "db_name": "admin",
        "config": {
            "host": "budget-generator-mongo",
            "port": 27017,
            "username": "dbuser",
            "password": "somepassword"
        }
    }
