'''Tests for the budget generating functions.'''
# get user data will be tested in a later commit
from application.home.common import generate_budget
from application.home.common.check import check_type

def test_check_type():
    user_data = {'savingsGoal':"7000", 'currentSaving':"700",'income':"300"}
    assert check_type(user_data) is True

def test_generate_budget():
    user_data = {'savingsGoal':"7000", 'currentSaving':"700",'income':"300"}
    assert generate_budget(user_data) == 21

def test_check_type_bad():
    user_data = {'savingsGoal':' ', 'currentSaving':' ','income':' '}
    assert check_type(user_data) is False

def test_generate_budget_bad():
    user_data = {'savingsGoal':' ', 'currentSaving':' ','income':' '}
    assert generate_budget(user_data) == "Please fill out all the categories with numbers"
