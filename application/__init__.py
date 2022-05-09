from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import create_engine



app = Flask(__name__)
app.secret_key = 'some_secret_password_Aksenof_love_db'
engine = create_engine("postgresql+psycopg2://root:pass@localhost/kino.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)

from application import models, routes

db.create_all()
