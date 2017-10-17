from flask import flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@localhost/tutorialdb'
db = SQLAlchemy(app)

class Heroes(db):
    __tablename__ = 'heroes'
class Creators(db):
    __tablename__ = 'creators'
class Series(db):
    __tablename__ = 'series'

