from application import create_app
from application.budget.model import Budget, QUERY_PARAMETERS_MAP
from mongoengine import connect
from datetime import datetime
import json
import pytest
import logging


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

def create_route_with_id(initialRoute, route_id=None):
	if not route_id:
		return initialRoute
	return f'{initialRoute}/{route_id}'

with open('application/tests/user_data.json') as file:
	TEST_DATA = json.load(file)


def test_budget_put(mock_get_db_connection):
    '''Testing that I can both put a budget into the
    database and retrieve it using the get budget route.'''
    flask_app = create_app()
    flask_app.testing = True
    test_data = TEST_DATA['user_db_data_good_post']

    with flask_app.test_client() as test_client:
        response_put = test_client.put(
            create_route_param('/budget', **test_data),
            follow_redirects=True
        )
        budget_put = json.loads(response_put.json)

        for key, val in QUERY_PARAMETERS_MAP.items():
            assert test_data[key] == budget_put[val]

        logging.warn(f'About to make get request {datetime.now()}')
        response_get = test_client.get(
        	create_route_with_id('/budget', budget_put['_id']),
        	follow_redirects=True
        )
        budget_get = json.loads(json.loads(response_get.get_data(['as text']))[0])
        
        assert budget_get == budget_put

def test_update_budget_with_id(mock_get_db_connection):
    flask_app = create_app()
    flask_app.testing = True
    test_data = TEST_DATA['user_db_data_good_post']
    update_data = TEST_DATA['user_db_data_good_update']

    with flask_app.test_client() as test_client:
        response_put = test_client.put(
            create_route_param('/budget', **test_data),
            follow_redirects=True
        )
        budget_put = json.loads(response_put.json)
        
        update_data_dict = {QUERY_PARAMETERS_MAP[x]:y for x, y in update_data.items()}
        assert update_data_dict == None
        response_update = test_client.post(
             create_route_param(
                f"/budget/{budget_put['_id']}",
                **{QUERY_PARAMETERS_MAP[x]:y for x, y in update_data.items()}
            ),
            follow_redirects=True
        )
        budget_update = json.loads(response_update.json)

        for key, val in QUERY_PARAMETERS_MAP.items():
            assert test_data[key] == budget_put[val]
        
        assert budget_update == update_data

# def test_budget_get_all(mock_get_db_connection):
# 	flask_app = create_app()
# 	flask_app.testing = True
#
# 	with flask_app.test_client() as test_client:
# 		test_client.put(
# 			create_route_param('/budget', **TEST_DATA['user_db_data_good_post']),
# 			follow_redirects=True
# 		)
# 		test_client.put(
# 			create_route_param('/budget', **TEST_DATA['user_db_data_good_post_2']),
# 			follow_redirects=True
# 		)
# 		returned_budget = test_client.put(
# 			create_route_param('/budget', **TEST_DATA['user_db_data_good_post_3']),
# 			follow_redirects=True
# 		)
# 		response_get = test_client.get(
# 			'/budget',
# 			follow_redirects=True
# 		)
# 		returned_budget = json_to_budget(returned_budget.get_data(['as_text']))
# 		print(response_get.get_data(['as_text']))
# 		assert returned_budget == {}
		# assert json_to_budget(response_get.get_data(['as_text'])[1:-1]) == returned_budget
