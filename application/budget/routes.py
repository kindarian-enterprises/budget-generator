'''This module will serve templates to a user
as well as decide what actions
should be taken depending on request type.'''

import application.budget.controller as controller
from flask import request, jsonify, after_this_request
from . import budget_bp


@budget_bp.route('/', methods=['PUT', 'GET'])
def budget_no_id() -> str:
    '''Routes requests for budget saving capabilities to the correct handler function.
       Returns a jsonified list or budet depending on request'''
    @after_this_request
    def allow_cors_access(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    method = request.method.lower()
    result = getattr(controller, f'{method}_budget_no_id')(request)
    return jsonify(result)

@budget_bp.route('/<string:budget_id>', methods=['GET', 'DELETE', 'POST'])
def budget_with_id(budget_id) -> str:
    '''Routes request for budget saving capabilities to the correct handler function.
       Returns a jsonified list, budget, or string depending on request'''
    method = request.method.lower()
    result = getattr(controller, f'{method}_budget_with_id')(budget_id, request)
    return jsonify(result)
