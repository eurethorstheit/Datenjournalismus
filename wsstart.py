#!/usr/bin/env python3
from flask import Flask, render_template, request, jsonify, url_for
from flask_bootstrap import Bootstrap
from flask_nav.elements import Navbar, View
from flask_nav import Nav
from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField
from flask_sqlalchemy import SQLAlchemy
from pydb import Navigator

topbar = Navbar('MDR-Project',
    View('Homepage / Index', 'index'),
    View('Testdb', 'testdb'),
    View('In Listenelemente einfügen','putinlistelements'),
    View('Auswahl und Reaktion','auswahl_reaktion'),
)

# Initialisierung Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey' # Notwendig fuer Forms

# Navigationsbar
nav = Nav(app)
nav.register_element('top',topbar)
nav.init_app(app)

# Initialize Database connection
dbNav = Navigator()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

# Ausprobierroute
@app.route("/testdb/")
def testdb():
    title = "Datenbankinhalte darstellen"
    # Get Data from DB
    data = dbNav.get_data_from_db('staedte_de_tiny').to_dict('r')

    return render_template("testdb.html",
                           title=title,
                           posts=data)

# Ausprobierroute zu Forms mit Daten
@app.route("/putinlistelements", methods=['GET','POST'])
def putinlistelements():
    title = "Datenbankinhalte darstellen"
    # Get Data from DB
    data = dbNav.get_data_from_db('staedte_de_tiny').to_dict('r')
    return render_template('putinlistelements.html',
                           title=title,
                           posts=data)

# Ausprobierroute mit Eingabe und Auswirkung ()
@app.route("/auswahl_reaktion", methods=['GET','POST'])
def auswahl_reaktion():
    title = "Auswahl mit Dropdown und Reaktion"
    # Get Data from DB
    data = dbNav.get_data_from_db('staedte_de_tiny').to_dict('r')
    return render_template('auswahl_reaktion.html',
                           title=title,
                           posts=data)


# Ausprobierroute mit variabler Unterseite
@app.route("/items/<item>")
def items(item):
    return '<h1>This is a Item Page. Item is: {}.'.format(item)


if __name__ == '__main__':
    Bootstrap(app)
    app.run(debug=True)


'''
https://www.youtube.com/watch?v=BFQfVd0g9sU
https://pythonspot.com/flask-web-forms/
'''

