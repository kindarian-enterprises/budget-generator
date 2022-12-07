from uuid import uuid4
import os
from mongoengine import Document, connect, IntField, DateTimeField, StringField
from datetime import datetime
from application.home.common.config import DATE_PATTERN
import logging
from datetime import datetime

DB_ROUTE = os.environ.get('DB_ROUTE', 'some default db route')
#OR we could drive this from config file, up to you

# request:DB
# TODO: refactor
QUERY_PARAMETERS_MAP = {
    "savingsGoal": "goal",
    "months": "timeUntilGoal",
    "spendingMoney": "monthlySpending",
    "toSave": "monthlySaving"
}

def get_db_connection(db_route=None):
    """
    Gets the DB connection
    """
    #do stuff to get db_route
    return connect(db_route)
    # This don't work this way!
    # Read https://docs.mongoengine.org/guide/connecting.html#connecting-to-mongodb

def query_params_to_budget(request_object):
    #extract budget dict from request query params
    logging.warning(f"{request_object} {datetime.now()}")
    result = {}
    request_dict = request_object.args.to_dict(flat=True)
    if request_dict:
        for key, val in QUERY_PARAMETERS_MAP.items():
            if key in request_dict:
                result[val] = request_dict[key]
    logging.warning(f"{result} {datetime.now()}")
    return result

class Budget(Document):
    goal = IntField(required=True)
    timeUntilGoal = IntField(required=True)
    monthlySpending = IntField(required=True)
    monthlySaving = IntField(required=True)
    dateCreated = DateTimeField(default=datetime.utcnow)
    id = StringField(
        primary_key=True,
        unique=True,
        default=str(uuid4())
    )
