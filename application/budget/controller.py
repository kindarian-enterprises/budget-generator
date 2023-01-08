from application.budget.model import Budget, query_params_to_budget
from flask import Request

def get_budget_no_id(request_object: Request) -> list:
    '''Gets all budgets and returns them in the form of
       a list of json strings.'''
    filters = query_params_to_budget(request_object)
    result = Budget.objects(**filters)

    return [x.to_json() for x in result]

def put_budget_no_id(request_object: Request) -> str:
    '''Creates a new object without a pre-specified ID.
       and returns a JSON string of that budget.'''
    budget_data = query_params_to_budget(request_object)
    budget_object = Budget(**budget_data).save()

    return budget_object.to_json()

def get_budget_with_id(budget_id: str, request_object: Request) -> list:
    '''Takes a request object and budget_id
       and returns either a specific budget or a list
       of budgets formed through query param filtering.'''
    filters = query_params_to_budget(request_object)
    filters.update({"id": budget_id})
    results = Budget.objects(**filters)
    return [x.to_json() for x in results]

def delete_budget_with_id(budget_id: str, request_object: Request) -> str:
    '''Takes a budget ID and deletes a specific object. Does not require request_object
       returns a string with budget id of deleted budget.'''
    budget = Budget.objects.get(id=budget_id)
    budget.delete()
    return f'Budget {budget_id} successfully deleted'

def post_budget_with_id(budget_id: str, request_object: Request) -> str:
    '''Takes a budget ID and request_object and updates a current budget
       with new information from the request_object. Returns a JSON string
       of the new budget.'''
    update = query_params_to_budget(request_object)
    budget = Budget.objects.get(id=budget_id)
    budget.modify(**update)
    budget.save()
    return budget.to_json()
