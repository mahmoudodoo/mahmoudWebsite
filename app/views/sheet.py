from flask.helpers import url_for
from app import app
from flask import render_template,flash, redirect
from app.forms.sheet_form import sheet_form
from app import db

@app.route('/sheet' ,methods=['GET', 'POST'])
def sheet():
    form = sheet_form()
    if form.validate_on_submit():
        sheet_link = form.sheet_link.data
        save_data(sheet_link)
    return render_template('sheet.html',form=form)



def save_data(sheet_link):
    print(sheet_link)
