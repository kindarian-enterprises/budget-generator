
from uuid import uuid4
import os
from mongoengine import Document, connect, IntField, dateTimeField


DB_ROUTE = os.environ.get('DB_ROUTE', 'some default db route')
#OR we could drive this from config file, up to you


def get_db_connection(db_route=None):
    #do stuff to get db_route
    return connect(db_route)
    # This don't work this way!
    # Read https://docs.mongoengine.org/guide/connecting.html#connecting-to-mongodb

def query_params_to_budget(request_object):
    #extract budget dict from request query params
    pass

class Budget(Document):
    goal = IntField()
    timeUntilGoal = IntField()
    monthlySpending = IntField()
    monthlySaving = IntField()
    dateCreated = dateTimeField()
    budgetId = StringField(
        primary_key=True,
        unique=True,
        default=str(uuid4())
    )
