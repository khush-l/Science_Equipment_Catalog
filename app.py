
import os
import flask
from flask import Flask, render_template, request, url_for, redirect
import logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import desc
import datetime


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
#function is used if there is an error in form data to go back to update it
def update_post(title = "", location = "", description = "", quantity = "", error = ""):
    return render_template("add_edit.html", ae_title=title, ae_location=location, ae_description = description, ae_quantity = quantity, ae_error=error)

@app.route('/', methods=["GET", "POST"])
def root():
    method = request.method
    if method == "GET":
        items = Items.query.all()
        processed_items = [(index, item, index % 2 == 0) for index, item in enumerate(items, start=0)]
        return render_template('home.html', items=processed_items)
    else:
        title = request.form["title"]
        location = request.form["location"]
        description = request.form["description"]
        quantity = request.form["quantity"]
        error = ""
        if title == "" or location == "":
            error = "Please provide both a title and a location"
            return(update_post(title=title,location=location,description=description, quantity=quantity,error=error))
        else:
            last_updated = datetime.datetime.now().replace(microsecond=0).isoformat(' ')
            insert = (title,description,location,last_updated,quantity)
            #need to still add the item
            items = Items.query.all()
            return render_template('home.html', items=items)
      
#this function gets called when you clock on edit and the id of the item is passed and it returns the add/edit page
@app.route('/item/<int:item_id>', methods=["GET", "POST"])
def item(item_id):
    item = Items.query.get_or_404(item_id)
    if request.method == 'POST':
        title = request.form["title"]
        location = request.form["location"]
        description = request.form["description"]
        quantity = request.form["quantity"]
        error = ""
        if title == "" or location == "":
            error = "Please provide both a title and a location"
            return update_post(title=title, location=location, description=description, quantity=quantity, error=error)
        else:
            item.title = title
            item.location = location
            item.description = description
            item.quantity = quantity
            db.session.commit()
            return redirect(url_for('root'))
    return render_template('add_edit.html', item=item)

@app.route('/add_item', methods=["GET", "POST"])
def add_item():
    if request.method == 'POST':
        title = request.form["title"]
        location = request.form["location"]
        description = request.form["description"]
        quantity = request.form["quantity"]
        error = ""
        if title == "" or location == "":
            error = "Please provide both a title and a location"
            return update_post(title=title, location=location, description=description, quantity=quantity, error=error)
        else:
            max_id_item = Items.query.order_by(desc(Items.id)).first()
            if max_id_item:
                next_id = max_id_item.id + 1
            else:
                next_id = 1
            last_updated = datetime.datetime.now().replace(microsecond=0)
            new_item = Items(id=next_id, title=title, description=description, location=location, last_updated=last_updated, quantity=quantity)
            db.session.add(new_item)
            db.session.commit()
            return redirect(url_for('root'))
    return render_template('add_edit.html', item=Items())
