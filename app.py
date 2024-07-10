from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(20), nullable=False)
    last_updated = db.Column(db.DateTime(timezone=True), server_default=func.now())
    quantity = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<Items {self.title}>'

@app.route('/', methods=["GET", "POST"])
def root():
    if request.method == "GET":
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
            return render_template("add_item.html", error=error)
        else:
            last_updated = datetime.datetime.now().replace(microsecond=0).isoformat(' ')
            new_item = Items(title=title, description=description, location=location, last_updated=last_updated, quantity=quantity)
            db.session.add(new_item)
            db.session.commit()
            return redirect(url_for('root'))

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
            return render_template("add_item.html", error=error)
        else:
            last_updated = datetime.datetime.now().replace(microsecond=0)
            new_item = Items(title=title, description=description, location=location, last_updated=last_updated, quantity=quantity)
            db.session.add(new_item)
            db.session.commit()
            return redirect(url_for('root'))
    return render_template('add_item.html', error="")

@app.route('/edit_item/<int:item_id>', methods=["GET", "POST"])
def edit_item(item_id):
    item = Items.query.get_or_404(item_id)
    if request.method == 'POST':
        title = request.form["title"]
        location = request.form["location"]
        description = request.form["description"]
        quantity = request.form["quantity"]
        error = ""
        if title == "" or location == "":
            error = "Please provide both a title and a location"
            return render_template("edit_item.html", item=item, error=error)
        else:
            item.title = title
            item.location = location
            item.description = description
            item.quantity = quantity
            db.session.commit()
            return redirect(url_for('root'))
    return render_template('edit_item.html', item=item, error="")

@app.route('/search', methods=["GET"])
def search():
    query = request.args.get('query')
    results = Items.query.filter(
        Items.title.contains(query) | 
        Items.description.contains(query) | 
        Items.location.contains(query)
    ).all()
    processed_items = [(index, item, index % 2 == 0) for index, item in enumerate(results, start=0)]
    return render_template('search_results.html', items=processed_items)

if __name__ == "__main__":
    app.run(debug=True)
