'''This module converts a html file to pdf'''
import pdfkit

def make_pdf(page):
    '''Expects a string to a html file and converts it to pdf'''
    my_pdf = pdfkit.from_file(page, False)
    return my_pdf
