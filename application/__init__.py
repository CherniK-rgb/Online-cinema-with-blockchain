from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = 'some_secret_password_Aksenof_love_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kino.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)

from application import models, routes

db.create_all()
