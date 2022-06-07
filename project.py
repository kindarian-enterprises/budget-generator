from flask import Flask

def create_app(testing = False):
	app = Flask(__name__)
	if testing:
		app.testing = True
	return app
