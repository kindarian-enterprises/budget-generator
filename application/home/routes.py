'''This module will serve templates to a user
as well as decide what actions
should be taken depending on request type.'''
from flask import render_template, request
from application.home.common import generate_budget, get_user_data
from . import home_bp

@home_bp.route('/')
def home():
    '''Will render the homepage template'''
    return render_template('index.jinja2')

@home_bp.route('/about')
def about():
    '''Will render the about page template'''
    return render_template('about.jinja2')

@home_bp.route('/form', methods=['GET', 'POST'])
def form():
    ''' Will render the form entry page template'''
    if request.method == 'GET':
        template = render_template('form.jinja2')
    else:
        user_data = get_user_data(request)
        response = generate_budget(user_data)
        # Different template will be rendered with info attained from generate_budget in future
        template = render_template('head.html')
    return template
