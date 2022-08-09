'''Tests for the budget generating functions.'''
# get user data will be tested in a later commit
import re
import json
from application.home.common.generate import generate_budget
from application.home.common.check import check_type
from application.home.common.convert_file import get_pdf_filename

with open('application/tests/user_data.json') as file:
	TEST_DATA = json.load(file)

def test_get_pdf_filename():
    pattern = re.compile(r'budget_gen_download_\d{14}\.pdf')
    assert pattern.search(get_pdf_filename())    

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
    assert generate_budget(user_data) is None

def test_generate_budget_invalid_amount():
    user_data = TEST_DATA["user_data_invalid_amount"]
    assert generate_budget(user_data) is None
