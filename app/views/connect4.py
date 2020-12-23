from flask.helpers import url_for
from app import app
from flask import render_template,flash, redirect


@app.route('/connect4')
def connect4():
    return render_template('games/connect4.html')


