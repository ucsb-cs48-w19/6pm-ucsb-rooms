from flask import Flask,request
from config import Config
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config.from_object(Config)
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import Room, Building
from app import routes
