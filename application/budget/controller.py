from application.budget.model import (Budget, query_params_to_budget,
                                      get_db_connection)

DB_CONNECTION = get_db_connection()

def get_budget_no_id(request_object):
    '''Gets all budgets'''
    results = Budget.objects()
    # TODO add optional filtering capabilities
    return results

def put_budget_no_id(request_object):
    '''Creates a new object without a pre-specified ID.'''
    budget_data = query_params_to_budget(request_object)

    budget_object = Budget(**budget_data).save()

    return budget_object

def get_budget_with_id(request_object):
    '''Takes a request object and returns a budget with a specific ID.'''
    results = Budget.objects(id=request_object.budget_id)
    return results

def delete_budget_with_id(request_object):
    '''Takes a budget ID and deletes a specific object.'''
    budget = Budget.objects(id=request_object.budget_id)
    budget.delete()
    return 'success'
    # TODO return success message
