from app.config import Config
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from pathlib import Path
from flask_login import LoginManager
from flask_moment import Moment




app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)
moment = Moment(app)



from app.models import user,post
from app.views import home,connect4,login,osStatus,register,sheet,xo,user,edit_profile,following,allPosts
from app.api import bp as api_bp


app.register_blueprint(api_bp, url_prefix='/api')