from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Length
from app import db



class sheet_form(FlaskForm):
    sheet_link = TextAreaField('Sheet id', validators=[Length(min=0, max=260)])
    submit = SubmitField('Save')



