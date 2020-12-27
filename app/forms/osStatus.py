from flask_wtf import FlaskForm
from wtforms import SubmitField


class osStatus_form(FlaskForm):
    printPdf = SubmitField('Print PDF')