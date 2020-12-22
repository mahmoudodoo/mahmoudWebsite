from app.config import Config
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask import render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

from app import models,views


@app.route('/')
def base():
    return render_template('base.html')
