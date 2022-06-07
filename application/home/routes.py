'''This module will serve templates to a user
as well as decide what actions
should be taken depending on request type.'''
from flask import Blueprint, render_template
from flask import current_app as app
from . import home_bp

@home_bp.route('/')
def home():
    '''Will render the homepage template'''
    return render_template('index.html')

@home_bp.route('/about')
def about():
    '''Will render the about page template'''
    return render_template('about.html')

if __name__ == '__main__':
    home_bp.run(debug=True)
