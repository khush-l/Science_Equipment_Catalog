import flask as fk
import logging
import sqlite3
import time
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = fk.Flask(__name__, '/static')
connection = sqlite3.connect("total.db")
cursor= connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, date_t TEXT, title TEXT, art TEXT)")

@app.route('/', methods=["GET", "POST"])
def root():
    method = fk.request.method
    if method == "GET":
        logging.info("********** root GET **********")
        return fk.render_template(
            'home.html',
            arts=[],
            error=""
        )
    else:
        return fk.render_template(
            'home.html',
            arts = [],
            error = ""
        )
#@app.route('/check', methods=["GET", "POST"])

