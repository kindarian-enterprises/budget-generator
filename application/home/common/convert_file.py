'''This module converts a html file to pdf'''
import os
import re
from flask import render_template
from datetime import datetime
import pdfkit
import shutil

TEMP_DIR = 'tmp'
FILE_DIR = 'budget-gen-files'
TARGET_DIR = os.path.join('/',TEMP_DIR, FILE_DIR)
DATE_PATTERN = "%Y%m%d%H%M%S"
CSS_FILE = '/home/edison/budgetGen/budget-generator/application/home/static/main.css'


def make_file_dir():
    if not os.path.isdir(TARGET_DIR):
        os.mkdir(TARGET_DIR)

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
    make_file_dir()
    html_string = render_template('get_pdf.html', result = mydict)
    pdf_filename = get_pdf_filename()
    my_pdf = os.path.join(TARGET_DIR, pdf_filename)
    pdfkit.from_string(html_string, my_pdf, css = CSS_FILE)
    return my_pdf

def pdf_cleanup():
    '''Used for periodic removal of generated files'''
    if os.path.isdir(TARGET_DIR):
        pattern = re.compile('\d+')
        file_list = os.listdir(TARGET_DIR)
        # List the files in TARGET_DIR

        for file in file_list:
        # Extract the integer timestamp
            match = pattern.search(file)
            my_date = int(match.group())
            if int(datetime.strftime(datetime.now(), DATE_PATTERN)) - 600 > my_date:
                # compare to current integer timestamp (same DATE_PATTERN)- some delta
                
                file_path = os.path.join(TARGET_DIR, file)
                os.remove(file_path)
                # delete those that fall outside the delta

def get_pdf_filename():
    now = datetime.now()
    return f'budget_gen_download_{datetime.strftime(now, DATE_PATTERN)}.pdf'
