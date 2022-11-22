'''This module will serve templates to a user
as well as decide what actions
should be taken depending on request type.'''

import application.budget.controller as controller
from flask import request, jsonify
from . import budget_bp

@budget_bp.route('/', methods=['PUT', 'GET'])
def budget_no_id():
    '''Routes requests for budget saving capabilities to the correct handler function.'''
    method = request.method.lower()
    result = getattr(controller, f'{method}_budget_no_id')(request)
    return jsonify(result) #may structure this differently

@budget_bp.route('/<string:budget_id>', methods=['GET', 'DELETE'])
def budget_with_id():
    #do stuff here
    method = request.method.lower()
    result = getattr(controller, f'{method}_budget_with_id')(request)
    return result
