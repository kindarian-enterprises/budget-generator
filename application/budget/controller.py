from application.budget.model import (Budget, query_params_to_budget,
                                      get_db_connection)
DB_CONNECTION = get_db_connection()

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
    # logging.warning('GOT HERE')
    # filters = query_params_to_budget(request_object)
    # logging.warning(f'{filters}')
    # filters.update({"id": budget_id})
    # logging.warning(f'{filters}')
    results = Budget.objects(id=budget_id)
    return [x.to_json() for x in results]

def delete_budget_with_id(budget_id, request_object):
    '''Takes a budget ID and deletes a specific object.'''
    budget = Budget.objects(id=budget_id)
    budget.delete()
    return f'Budget {budget_id} successfully deleted'
