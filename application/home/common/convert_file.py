'''This module converts a html file to pdf'''
import os
import re
from datetime import datetime
from flask import render_template
from weasyprint import HTML, CSS
from application.home.common.config import APPCONFIG, STATIC_DIR, DATE_PATTERN

TEMP_DIR = 'tmp'
FILE_DIR = 'budget-gen-files'
TARGET_DIR = os.path.join('/',TEMP_DIR, FILE_DIR)
CSS_FILE = os.path.join(STATIC_DIR, 'main.css')

def make_file_dir() -> None:
    '''Creates TARGET_DIR if not already made.
       Returns nothing.'''
    if not os.path.isdir(TARGET_DIR):
        os.mkdir(TARGET_DIR)

def make_pdf(budget_info: dict) -> str:
    '''Expects a dictionary of query parameters required to render the budget
        page template. Returns a string filepath to the created PDF'''

    make_file_dir()

    # Create our html with budget info for pdf
    html_string = render_template('get_pdf.html', result = budget_info)

    # Create a pdf filename based on the current time
    pdf_filename = get_pdf_filename()
    my_pdf = os.path.join(TARGET_DIR, pdf_filename)
    # Create pdf and return the location of that pdf as a string
    with open(CSS_FILE) as css:
        HTML(string=html_string).write_pdf(my_pdf, stylesheets=[CSS(string=css.read())])
    return my_pdf

def pdf_cleanup() -> None:
    '''Used for periodic removal of generated files'''
    if os.path.isdir(TARGET_DIR):
        pattern = re.compile(APPCONFIG['filename']['file_pattern'])
        file_list = os.listdir(TARGET_DIR)
        # List the files in TARGET_DIR

        for file in file_list:
        # Extract the integer timestamp
            match = pattern.search(file)
            if match:
                my_date = int(match.groups()[0])
                if int(datetime.strftime(datetime.now(), DATE_PATTERN)) - 300 > my_date:
                # compare to current integer timestamp (same DATE_PATTERN)- some delta

                    file_path = os.path.join(TARGET_DIR, file)
                    os.remove(file_path)
                    # delete those that fall outside the delta

def get_pdf_filename() -> str:
    '''Generates and returns a string for
       pdf filename using the current time'''
    now = datetime.now()
    return f'budget_gen_download_{datetime.strftime(now, DATE_PATTERN)}.pdf'
