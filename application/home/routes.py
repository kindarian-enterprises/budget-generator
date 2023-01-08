'''This module will serve templates to a user
as well as decide what actions
should be taken depending on request type.'''
from flask import render_template, request, send_file
from application.home.common.generate import generate_budget, get_user_data
from application.home.common.convert_file import make_pdf, pdf_cleanup
from . import home_bp

@home_bp.route('/')
def home() -> str:
    '''Will render the homepage as an HTML string.'''
    return render_template('index.jinja2')

@home_bp.route('/about')
def about() -> str:
    '''Will render the about page as an HTML string.'''
    return render_template('about.jinja2')

@home_bp.route('/form', methods=['GET'])
def form() -> str:
    ''' Will render the form entry page as an HTML string.'''
    return render_template('form.jinja2')

@home_bp.route('/display', methods=['POST'])
def display() -> str:
    '''Will render the budget display page with info from form page
       as an HTML string'''
    user_data = get_user_data(request)
    response = generate_budget(user_data)
    result = {**user_data, **response}

    # TODO: We'll need to use common.config.APPCONFIG to get app_url so that we
    #  can build the button target
    template = render_template('display.html', result = result)
    return template

@home_bp.route('/getpdf', methods=['GET'])
def getpdf():
    '''Given query parameters save, spend, timetogoal, and goal, we will
        generate a pdf file and return it as a filestream download.'''

    query_params = request.args.to_dict(flat=True)
    pdf_cleanup()
    file_path = make_pdf(query_params)

    return send_file(file_path, download_name='your_budget.pdf')

@home_bp.route('/budgets', methods=['PUT', 'GET'])
def budgets() -> str:
    '''Will save query params as budget to database if method = PUT then
       render html template for saved budgets page. JS file will take care of
       rendering and deletion of budgets in list'''
    if request.method == 'GET':
        template = render_template('saved_budgets.html')
    else:
        pass
    return template
