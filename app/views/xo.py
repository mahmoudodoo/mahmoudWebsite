from flask.helpers import url_for
from app import app
from flask import render_template,flash, redirect


@app.route('/xo')
def xo():
    return render_template('games/xo.html')