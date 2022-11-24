from uuid import uuid4
import os
from mongoengine import Document, connect, IntField, DateTimeField, StringField
from datetime import datetime
from application.home.common.config import DATE_PATTERN


DB_ROUTE = os.environ.get('DB_ROUTE', 'some default db route')
#OR we could drive this from config file, up to you


def get_db_connection(db_route=None):
    #do stuff to get db_route
    return connect(db_route)
    # This don't work this way!
    # Read https://docs.mongoengine.org/guide/connecting.html#connecting-to-mongodb

def query_params_to_budget(request_object):
    #extract budget dict from request query params
    request_dict = request_object.args.to_dict(flat=True)
    if not request_dict:
        request_dict = request_object.json()
    
    if request_dict:
        result = {
            "goal":request_dict['savingsGoal'],
            "timeUntilGoal":request_dict['months'],
            "monthlySpending":request_dict['spendingMoney'],
            "monthlySaving":request_dict['toSave'],
            # "dateCreated": datetime.strftime(now, DATE_PATTERN)
        }
        return result
    raise Exception("Request contained no arguments")

class Budget(Document):
    goal = IntField()
    timeUntilGoal = IntField()
    monthlySpending = IntField()
    monthlySaving = IntField()
    dateCreated = DateTimeField(default=datetime.utcnow)
    id = StringField(
        primary_key=True,
        unique=True,
        default=str(uuid4())
    )
