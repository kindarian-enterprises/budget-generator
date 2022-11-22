from application import create_app
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


with open('application/tests/user_data.json') as file:
	TEST_DATA = json.load(file)

def test_budget_put_no_id(mock_get_db_connection):
	flask_app = create_app()
	flask_app.testing= True

	with flask_app.test_client() as test_client:
		response = test_client.put(
			'/budget',
			data=TEST_DATA['user_db_data_good_post'],
			follow_redirects=True
		)
		assert response.get_json() == {}
