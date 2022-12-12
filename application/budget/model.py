from uuid import uuid4
import os
from mongoengine import Document, connect, IntField, DateTimeField, StringField
from datetime import datetime
from application.home.common.config import DATE_PATTERN
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

def front_end_params_to_back_end(parameters):
    return_value = {}
    for front, back in QUERY_PARAMETERS_MAP.items():
        if front in parameters:
            return_value[f"{back}"] = parameters[f"{front}"]
    return return_value

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
    result = {}
    request_dict = request_object.args.to_dict(flat=True)
    if request_dict:
        result = front_end_params_to_back_end(request_dict)
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
