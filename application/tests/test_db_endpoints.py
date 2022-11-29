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

def create_route_with_id(initialRoute, route_id = None):
	if not route_id:
		return initialRoute
	return f'{initialRoute}/{route_id}'

with open('application/tests/user_data.json') as file:
	TEST_DATA = json.load(file)


def test_budget_put_and_get(mock_get_db_connection):
	'''Testing that I can both put a budget into the
	database and retrieve it using the get budget route.'''
	flask_app = create_app()
	flask_app.testing= True
	_test_data = TEST_DATA['user_db_data_good_post']

	with flask_app.test_client() as test_client:
		response_put = test_client.put(
			create_route_param('/budget', **_test_data),
			follow_redirects=True
		)
		budget_put = json_to_budget(response_put.get_data(['as_text']))
		response_get = test_client.get(
			create_route_with_id('/budget', budget_put.id),
			follow_redirects=True
		)
		budget_get = json_to_budget(response_get.get_data(['as_text'])[1:-1])
		
		assert budget_put.goal == int(_test_data['savingsGoal'])
		assert budget_put.timeUntilGoal == int(_test_data['months'])
		assert budget_put.monthlySpending == int(_test_data['spendingMoney'])
		assert budget_put.monthlySaving == int(_test_data['toSave'])
		assert budget_get.id == budget_put.id

def test_budget_get_all(mock_get_db_connection):
	flask_app = create_app()
	flask_app.testing = True

	with flask_app.test_client() as test_client:
		test_client.put(
			create_route_param('/budget', **TEST_DATA['user_db_data_good_post']),
			follow_redirects=True
		)
		test_client.put(
			create_route_param('/budget', **TEST_DATA['user_db_data_good_post_2']),
			follow_redirects=True
		)
		returned_budget = test_client.put(
			create_route_param('/budget', **TEST_DATA['user_db_data_good_post_3']),
			follow_redirects=True
		)
		response_get = test_client.get(
			'/budget',
			follow_redirects=True
		)
		returned_budget = json_to_budget(returned_budget.get_data(['as_text']))
		print(response_get.get_data(['as_text']))
		assert returned_budget == {}
		# assert json_to_budget(response_get.get_data(['as_text'])[1:-1]) == returned_budget