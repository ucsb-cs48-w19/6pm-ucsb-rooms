from flask import Flask,request
from config import Config
from flask_sqlalchemy import SQLAlchemy
#from asn1crypto._ffi import null
#import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config.from_object(Config)
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import Room, Building
from app import routes

# This line will force create the database. For local testing.
#db.create_all()

# Setup some test rooms and buildings.
#print(help(Building.query.filter_by(name='HFH')))

if (len(Building.query.filter_by(name='HFH').all()) == 0):
    b1 = Building(name='HFH')
    db.session.add(b1)
    r1 = Room('9001','3:00-6:00pm', 'trashy_room_standard',b1.id)
    db.session.add(r1)
    db.session.commit();