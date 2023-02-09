import json
from application.tests.conftest import (
    HOME_PAGE_TEST_DATA,
    ABOUT_PAGE_TEST_DATA,
    FORM_PAGE_TEST_DATA,
    DISPLAY_PAGE_TEST_DATA,
    SAVED_BUDGETS_PAGE_TEST_DATA,
    DASHBOARD_PAGE_TEST_DATA
)
from application import create_app

with open('application/tests/user_data.json') as file:
	TEST_DATA = json.load(file)

def test_home_page():
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.get_data(as_text=True) == HOME_PAGE_TEST_DATA


def test_about_page():
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        response = test_client.get('/about')
        assert response.get_data(as_text=True) == ABOUT_PAGE_TEST_DATA

def test_form_page():
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        response = test_client.get('/form')
        assert response.get_data(as_text=True) == FORM_PAGE_TEST_DATA

def test_post_display_page():
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        response = test_client.post(
            '/display',
            data = TEST_DATA['user_data_good_post'],
            follow_redirects = True
        )
        assert response.get_data(as_text=True) == DISPLAY_PAGE_TEST_DATA

def test_get_saved_budgets_page():
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        response = test_client.get(
            '/saved-budgets',
            follow_redirects = True
        )
        print(response.get_data(as_text=True))
        assert response.get_data(as_text=True) == SAVED_BUDGETS_PAGE_TEST_DATA

def test_get_dashboard_page():
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        response = test_client.get(
            '/dashboard',
            follow_redirects = True
        )
    assert response.get_data(as_text=True) == DASHBOARD_PAGE_TEST_DATA

'''These bottom tests either all return a method not allowed response,
   or in the case of the get pdf page a check on the response body cannot
   be made.'''

def test_post_form_page():
    '''Test will eventually have a different page loaded as response...
        for now post request will return 200'''
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        response = test_client.post(
            '/form',
            data = TEST_DATA['user_data_good_post'],
            follow_redirects = True
        )
        assert response.status_code == 405

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

def test_get_display_page():
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        response = test_client.get('/display')
        assert response.status_code == 405

def test_get_pdf_page():
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
        response = test_client.get(
            '/getpdf',
            data = TEST_DATA['user_pdf_data'],
            follow_redirects = True
        )
        assert response.status_code == 200
