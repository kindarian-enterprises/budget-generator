'''This module will serve templates to a user
as well as decide what actions
should be taken depending on request type.'''
from flask import Blueprint, render_template, request
from flask import current_app as app
from . import home_bp
from application.home.common import generate_budget

@home_bp.route('/')
def home():
    '''Will render the homepage template'''
    return render_template('index.jinja2')

@home_bp.route('/about')
def about():
    '''Will render the about page template'''
    return render_template('about.jinja2')

@home_bp.route('/form', methods=['GET', 'POST'])
def form():
    ''' Will render the form entry page template'''
    if request.method == 'GET':
        template = render_template('form.jinja2')
    else:
        income = request.form.get("month")
        payments = request.form.get("monthPay")
        curr_saving = request.form.get("savings")
        desired_spending = request.form.get("spending")
        savings_goal = request.form.get("savingGoal")

        user_data = {"income":income, "monthPay":payments, "currentSaving":curr_saving, "spendingMoney":desired_spending, "savingsGoal":savings_goal}
        # response = budget_gen.generate_budget(user_data)
        template = render_template('form.jinja2')
    return template
