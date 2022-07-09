'''Tests for the budget generating functions.'''
# get user data will be tested in a later commit
import json
from application.home.common.generate import generate_budget
from application.home.common.check import check_type

with open('application/tests/user_data.json') as file:
	TEST_DATA = json.load(file)

def test_check_type():
    user_data = TEST_DATA["user_data_good"]
    assert check_type(user_data) is True

def test_generate_budget():
    user_data = TEST_DATA["user_data_good"]
    assert generate_budget(user_data) == {"months": 32, "toSave": 200}

def test_check_type_bad():
    user_data = TEST_DATA["user_data_bad"]
    assert check_type(user_data) is False

def test_generate_budget_bad_data():
    user_data = TEST_DATA["user_data_bad"]
    assert generate_budget(user_data) == None

def test_generate_budget_invalid_amount():
    user_data = TEST_DATA["user_data_invalid_amount"]
    assert generate_budget(user_data) == None
