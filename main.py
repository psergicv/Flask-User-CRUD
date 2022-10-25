from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(35), nullable=False)
    lastname = db.Column(db.String(35), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Author: {self.firstname}>'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(90), nullable=False)
    intro = db.Column(db.String(180), nullable=False)
    text = db.Column(db.String(800), nullable=False)
    created_date = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<Title: {self.title}>'
