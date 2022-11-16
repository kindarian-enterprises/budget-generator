
from application.budget.model import (Budget, query_params_to_budget,
                                      get_db_connection)

DB_CONNECTION = get_db_connection()

def get_budget_no_id(request_object):
    #do getty kind of stuff, like extract filters from keyword arguments, etc
    results = Budget.objects()
    return results

def put_budget_no_id(request_object):

    budget_data = query_params_to_budget(request_object)

    budget_object = Budget(**budget_data).save()

    return budget_object
