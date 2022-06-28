import json
from application import create_app

with open('application/tests/user_data.json') as file:
	TEST_DATA = json.load(file)

def test_home_page():
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200


def test_about_page():
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        response = test_client.get('/about')
        assert response.status_code == 200

def test_form_page():
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        response = test_client.get('/form')
        assert response.status_code == 200

def test_post_form_page():
    '''Test will eventually have a different page loaded as response...
        for now post request will return 200'''
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        response = test_client.post('/form', data = TEST_DATA['user_data_good_post'], follow_redirects = True)
        assert response.status_code == 200

def test_post_home_page():
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        response = test_client.post('/')
        assert response.status_code == 405


def test_post_about_page():
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        response = test_client.post('/about')
        assert response.status_code == 405
