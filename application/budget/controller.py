from application.budget.model import Budget, query_params_to_budget

from application.budget.db import get_db_connection

get_db_connection()

def get_budget_no_id(request_object):
    '''Gets all budgets'''
    filters = query_params_to_budget(request_object)
    result = Budget.objects(**filters)

    return [x.to_json() for x in result]

def put_budget_no_id(request_object):
    '''Creates a new object without a pre-specified ID.'''
    budget_data = query_params_to_budget(request_object)
    budget_object = Budget(**budget_data).save()

    return budget_object.to_json()

def get_budget_with_id(budget_id, request_object):
    '''Takes a request object and returns a budget with a specific ID.'''
    filters = query_params_to_budget(request_object)
    filters.update({"id": budget_id})
    results = Budget.objects(**filters)
    return [x.to_json() for x in results]

def delete_budget_with_id(budget_id, request_object):
    '''Takes a budget ID and deletes a specific object.'''
    budget = Budget.objects.get(id=budget_id)
    budget.delete()
    return f'Budget {budget_id} successfully deleted'

def post_budget_with_id(budget_id, request_object):
    update = query_params_to_budget(request_object)
    budget = Budget.objects.get(id=budget_id)
    budget.modify(**update)
    budget.save()
    return budget.to_json()
