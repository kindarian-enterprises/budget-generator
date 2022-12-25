from uuid import uuid4
from mongoengine import Document, IntField, DateTimeField, StringField
from datetime import datetime
from application.home.common.config import DATE_PATTERN
from bson.objectid import ObjectId


# request:DB
# TODO: refactor
QUERY_PARAMETERS_MAP = {
    "savingsGoal": ("goal", int),
    "months": ("timeUntilGoal", int),
    "spendingMoney": ("monthlySpending", int),
    "toSave": ("monthlySaving", int)
}

def get_object_id():
    return str(ObjectId())

def front_end_params_to_back_end(parameters):
    return_value = {}
    for front, back in QUERY_PARAMETERS_MAP.items():
        if front in parameters:
            return_value[f"{back[0]}"] = back[1](parameters[f"{front}"])
    return return_value


def query_params_to_budget(request_object):
    #extract budget dict from request query params
    result = {}
    request_dict = request_object.args.to_dict(flat=True)
    request_json = request_object.json
    if request_dict:
        result = front_end_params_to_back_end(request_dict)
    elif request_json:
        result = front_end_params_to_back_end(dict(request_json))
    return result

class Budget(Document):
    goal = IntField(required=True)
    timeUntilGoal = IntField(required=True)
    monthlySpending = IntField(required=True)
    monthlySaving = IntField(required=True)
    dateCreated = DateTimeField(default=datetime.utcnow)
    id = StringField(
        primary_key=True,
        default=get_object_id
    )
