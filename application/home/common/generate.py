"""Module is used for handling user input to the budget form."""

from application.home.common.check import check_type
def generate_budget(user_data):
    """Takes the user data and does some calculations to reach desired goals set."""
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

def get_user_data(req):
    '''Obtains user data from a request.'''
    income = req.form.get("month")
    payments = req.form.get("monthPay")
    curr_saving = req.form.get("savings")
    desired_spending = req.form.get("spending")
    savings_goal = req.form.get("savingGoal")
    return {"income":income, "monthPay":payments, "currentSaving":curr_saving, "spendingMoney":desired_spending, "savingsGoal":savings_goal}
