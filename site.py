'''This module will serve templates to a user
as well as decide what actions
should be taken depending on request type.'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	'''Will render the homepage template'''
	return render_template('index.html')

@app.route('/about')
def about():
	'''Will render the about page template'''
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)
