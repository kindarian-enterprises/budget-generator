from application import create_app

def test_home_page():
    flask_app = create_app()
    flask_app.testing = True

    with flask_app.test_client() as test_client:
	    response = test_client.get('/')
	    assert response.status_code == 200
