'''This module converts a html file to pdf'''
import pdfkit
import shutil
import os

def make_pdf(**kwargs):
    '''Expect a dictionary of query parameters required to render the budget
        page template'''

    """

        Use the key-value pairs, we'll use some permutation of
            result = {**user_data, **response}
            template = render_template('display.html', result = result)
             and some of my_pdf = pdfkit.from_file(page, False)
        in order to obtain our HTML for rendering.

    """

    shutil.copy('fake_pdf.pdf', '/tmp/fake_pdf.pdf')
    my_pdf = '/tmp/fake_pdf.pdf'
    return my_pdf

def pdf_cleanup():
    '''Used for periodic removal of generated files'''

    # TODO: Based on configurable timeout, we will  inspect the timestamp of the file,
    #  perhaps in its naming convention, deleting any that are too old
    os.remove('/temp/fake_pdf.pdf')
