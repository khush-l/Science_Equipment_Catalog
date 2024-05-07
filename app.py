
import os
import flask
from flask import Flask, render_template, request, url_for, redirect
import logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(20), nullable=False)
    last_updated = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    quantity = db.Column(db.Integer, nullable = True)

    def __repr__(self):
        return f'<Items {self.title}>'

@app.route('/', methods=["GET", "POST"])
def root():
    method = flask.request.method
    if method == "GET":
        items = Items.query.all()
        return render_template('home.html', items=items)
    
#@app.route('/check', methods=["GET", "POST"])

