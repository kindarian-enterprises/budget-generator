from application import create_app
from application.budget.model import Budget
import json
import pytest
from mongoengine import connect

@pytest.fixture()
def mock_get_db_connection(mocker):
    return mocker.patch(
		'application.budget.model.get_db_connection',
		return_value=connect(
			'mongoenginetest',
			host='mongomock://localhost'
			)
		)

def json_to_budget(jsonString):
    return Budget.from_json(jsonString, created=True)

def create_route_param(initialRoute, **params):
    if not params:
        return initialRoute
    result = f'{initialRoute}?'
    for key, value in params.items():
        result += f'{key}={value}&'
    return result[:-1]

with open('application/tests/user_data.json') as file:
	TEST_DATA = json.load(file)


def test_budget_put_no_id(mock_get_db_connection):
	flask_app = create_app()
	flask_app.testing= True

	with flask_app.test_client() as test_client:
		response = test_client.put(
			create_route_param('/budget', **TEST_DATA['user_db_data_good_post']),
			follow_redirects=True
		)
		budget = json_to_budget(response.get_data(['as_text']))
		assert budget.goal == 7000
		assert budget.timeUntilGoal == 10
		assert budget.monthlySpending == 400
		assert budget.monthlySaving == 700
