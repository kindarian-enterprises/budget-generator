"""Module is used for handling user input to the budget form."""
from flask import Request

from application.home.common.check import check_type
def generate_budget(user_data: dict) -> dict:
    """Takes the user data in the form of a dictionary
       and returns a dictionary of values based off of
       the desired goals set."""
    response = None
    count = 0

    if check_type(user_data):
        goal = int(user_data['savingsGoal'])
        curr_saving = int(user_data['currentSaving'])
        pay = int(user_data['income'])
        spending_money = int(user_data['spendingMoney'])
        month_pay = int(user_data['monthPay'])
        if curr_saving < goal:
            if pay - (month_pay + spending_money) > 0:
                while curr_saving < goal:
                    count += 1
                    curr_saving = (curr_saving + pay) - (spending_money + month_pay)
                response = {"months": count, "toSave": pay - (spending_money + month_pay)}
    return response

def get_user_data(request_object: Request) -> dict:
    '''Obtains user data from a request_object and returns
       a dictionary of the request data.'''
    income = request_object.form.get("month")
    payments = request_object.form.get("monthPay")
    curr_saving = request_object.form.get("savings")
    desired_spending = request_object.form.get("spending")
    savings_goal = request_object.form.get("savingGoal")
    return {"income":income, "monthPay":payments, "currentSaving":curr_saving, "spendingMoney":desired_spending, "savingsGoal":savings_goal}
