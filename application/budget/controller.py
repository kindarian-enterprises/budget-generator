from flask import Request
from voluptuous import MultipleInvalid
from application.budget.model import Budget, query_params_to_budget, BUDGET_DATA_SCHEMA
from application.budget.common.exceptions import FailedSchemaException
from application.budget.common.pipelines import make_pagination_pipeline

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
    try:
        BUDGET_DATA_SCHEMA(budget_data)
    except MultipleInvalid:
        raise FailedSchemaException("Budget data did not conform to schema")
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

def get_budgets_page(page_size, page_number, filters = None):
    '''Takes filters to search on, and a page size / page number
       then returns a "page" of documents matching the filters.'''
    offset = None
    if filters is None:
        filters = {}
    if page_number == 1:
        offset = 0
    else:
        offset = (page_size * page_number) - page_size

    pipeline = make_pagination_pipeline(offset, page_size, filters)

    query_result = Budget.objects().aggregate(pipeline)

    result = list(query_result)
    return result
