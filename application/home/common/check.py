'''Module will be used to check the types of the user data as to make sure that there are no strings or empty values'''

def check_type(user_data):
    confirmation = True
    try:
        goal = int(user_data['savingsGoal'])
    except ValueError:
        confirmation = False
    try:
        curr_saving = int(user_data['currentSaving'])
    except ValueError:
        confirmation = False
    try:
        pay = int(user_data['income'])
    except ValueError:
        confirmation = False
    return confirmation
