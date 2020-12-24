from flask.helpers import url_for
from app import app
from flask import render_template,flash, redirect
from app.forms.sheet_form import sheet_form
from app import db
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
from app.models.user import Users




@app.route('/sheet' ,methods=['GET', 'POST'])
def sheet():
    form = sheet_form()
    with open('app/credentials.json')as f :
        data = json.load(f)
        client_email= data['client_email']

    scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('app/credentials.json',scope)
    client = gspread.authorize(creds)
    sheet = client.open('Users').sheet1
    if form.validate_on_submit():
        save_data(sheet)
    return render_template('sheet.html',form=form,client_email =client_email)



def save_data(sheet):
    sheet.clear()
    users = Users.query.all()
    data = []
    for user in users:
        data.append([user.id,user.username,user.email])
        print(user.username)
    sheet.insert_row(['ID','Username','Email'],1)
    sheet.insert_rows(data,2)
    
