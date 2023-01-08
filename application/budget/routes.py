'''This module will serve templates to a user
as well as decide what actions
should be taken depending on request type.'''

import application.budget.controller as controller
from flask import request, jsonify
from . import budget_bp
from datetime import datetime


@budget_bp.route('/', methods=['PUT', 'GET'])
def budget_no_id() -> str:
    '''Routes requests for budget saving capabilities to the correct handler function.
       Returns a jsonified list or budet depending on request'''
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
