'''This module will serve templates to a user
as well as decide what actions
should be taken depending on request type.'''

from http import HTTPStatus
from flask import request, jsonify, after_this_request
from application.budget.controller import InvalidPayloadError
import application.budget.controller as controller
from . import budget_bp


@budget_bp.route('/', methods=['PUT', 'GET'])
def budget_no_id() -> str:
    '''Routes requests for budget saving capabilities to the correct handler function.
       Returns a jsonified list or budget depending on request'''
    @after_this_request
    def allow_cors_access(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
    return_value = None
    method = request.method.lower()
    try:
        result = getattr(controller, f'{method}_budget_no_id')(request)
        return_value = jsonify(result)
    except InvalidPayloadError as err:
        return jsonify(str(err), HTTPStatus.BAD_REQUEST)
    except Exception as err:
        return jsonify(str(err), HTTPStatus.INTERNAL_SERVER_ERROR)

    return return_value

@budget_bp.route('/<string:budget_id>', methods=['GET', 'DELETE', 'POST'])
def budget_with_id(budget_id) -> str:
    '''Routes request for budget saving capabilities to the correct handler function.
       Returns a jsonified list, budget, or string depending on request'''
    return_value = None
    method = request.method.lower()
    try:
        result = getattr(controller, f'{method}_budget_with_id')(budget_id, request)
        return_value = jsonify(result)
    except InvalidPayloadError as err:
        return jsonify(str(err), HTTPStatus.BAD_REQUEST)
    except Exception as err:
        return jsonify(str(err), HTTPStatus.INTERNAL_SERVER_ERROR)

    return return_value
