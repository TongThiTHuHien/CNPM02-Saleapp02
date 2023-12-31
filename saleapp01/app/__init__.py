from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)
app.secret_key = 'sjbda@$3ejksfhklsd@#@$#TFsifjsdfhs'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:%s@localhost/saledbv1?charset=utf8mb4' % quote('10072003')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
login = LoginManager(app=app)
