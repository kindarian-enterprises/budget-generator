'''This module converts a html file to pdf'''
from flask import render_template
from datetime import datetime
import pdfkit
import shutil
import os

def make_pdf(mydict):
    '''Expect a dictionary of query parameters required to render the budget
        page template'''

    """

        Use the key-value pairs, we'll use some permutation of
            result = {**user_data, **response}
            template = render_template('display.html', result = result)
             and some of my_pdf = pdfkit.from_file(page, False)
        in order to obtain our HTML for rendering.

    """
    template = render_template('display.html', result = mydict)
    pdf_location = get_pdf_date()
    pdfkit.from_string(template, pdf_location)
    shutil.copy(pdf_location, '/tmp/' + pdf_location)
    my_pdf = '/tmp/' + pdf_location
    return my_pdf

def pdf_cleanup():
    '''Used for periodic removal of generated files'''
    pdf_location = get_pdf_date()
    now = datetime.now()
    if pdf_location[:-4] < datetime.strftime(now, "%m%d%Y%H%M%S") - 600:
        os.remove('/tmp/' + pdf_location)
    else:
        pass

def get_pdf_date() {
    now = datetime.now()
    return datetime.strftime(now, "%m%d%Y%H%M%S") + '.pdf'
}