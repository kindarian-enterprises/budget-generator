from flask import Flask


def test_home_page():
	flask_app = Flask('/home/edison/budgetGen/budget_generator/site')
	flask_app.testing = True

	with flask_app.test_client() as test_client:
		response = test_client.get('/')
		assert response.status_code == 404
	