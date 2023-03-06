from mongoengine import Document, IntField, DateTimeField, StringField
from voluptuous import Schema, All, Range, Required, ALLOW_EXTRA
from datetime import datetime
from bson.objectid import ObjectId
from flask import Request


# request:DB
# TODO: refactor
QUERY_PARAMETERS_MAP = {
    "savingsGoal": ("goal", int),
    "months": ("timeUntilGoal", int),
    "spendingMoney": ("monthlySpending", int),
    "toSave": ("monthlySaving", int)
}

def get_object_id() -> str:
    '''Returns an ObjectId converted to a string.'''
    return str(ObjectId())

def front_end_params_to_back_end(parameters: dict) -> dict:
    '''Takes a dictionary from the front end and renames
       the parameters to work with the backend mongoEngine Document.'''
    return_value = {}
    for front, back in QUERY_PARAMETERS_MAP.items():
        if front in parameters:
            return_value[f"{back[0]}"] = back[1](parameters[f"{front}"])
    return return_value


def query_params_to_budget(request_object: Request) -> dict:
    '''Extracts budget dict from request query params. Returns a dictionary
       of budget-ready query parameters.'''
    result = {}
    request_dict = request_object.args.to_dict(flat=True)
    if request_dict:
        result = front_end_params_to_back_end(request_dict)
    try:
        request_json = request_object.json
        if request_json:
            result = front_end_params_to_back_end(dict(request_json))
    except:
        #TODO Add logging for errors
        print('Could not load any JSON from query_params_to_budget')
    return result

CREATE_BUDGET_SCHEMA = Schema({
    Required('goal'): All(int, Range(min=1)),
    Required('timeUntilGoal'): All(int, Range(min=1)),
    Required('monthlySpending'): All(int, Range(min=0)),
    Required('monthlySaving'): All(int, Range(min=1))
    }
)

FILTER_BUDGET_SCHEMA = Schema({
    'goal': All(int, Range(min=1)),
    'timeUntilGoal': All(int, Range(min=1)),
    'monthlySpending': All(int, Range(min=0)),
    'monthlySaving': All(int, Range(min=1))
    },
    extra=ALLOW_EXTRA
)

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
