'''This module will serve templates to a user
as well as decide what actions
should be taken depending on request type.'''

import application.budget.controller as controller
from flask import request, jsonify
from . import budget_bp
import logging
from datetime import datetime

@budget_bp.route('/', methods=['PUT', 'GET'])
def budget_no_id():
    '''Routes requests for budget saving capabilities to the correct handler function.'''
    method = request.method.lower()
    result = getattr(controller, f'{method}_budget_no_id')(request)
    return jsonify(result)

@budget_bp.route('/<string:budget_id>', methods=['GET', 'DELETE', 'POST'])
def budget_with_id(budget_id):
    #do stuff here
    method = request.method.lower()
    logging.warning(f'{request} {datetime.now()}')
    logging.warning('about to run get_budget_with_id')
    result = getattr(controller, f'{method}_budget_with_id')(budget_id, request)
    return jsonify(result)
