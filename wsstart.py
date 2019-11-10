#!/usr/bin/env python3
import json
import os
from flask import Flask, render_template, request, jsonify, url_for
from flask_bootstrap import Bootstrap
from flask_nav.elements import Navbar, View
from flask_nav import Nav
from flask_bootstrap import WebCDN



from flask_wtf import FlaskForm
from sqlalchemy.exc import DatabaseError
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
Bootstrap(app)
app.extensions['bootstrap']['cdns']['jquery'] = \
    WebCDN('https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/')
app.extensions['bootstrap']['cdns']['data_tables'] = \
    WebCDN("https://cdn.datatables.net/1.10.20/js/jquery.dataTables.js")
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
app.config['SECRET_KEY'] = 'secretkey' # Notwendig fuer Forms


# Navigationsbar
nav = Nav(app)
nav.register_element('top',topbar)
nav.init_app(app)

# Initialize Database connection

with app.open_resource('static/config/connection_config.json') as json_data_file:
    data = json.load(json_data_file)
try:
    connection_prop = data['mysql']
    dbNav = Navigator(connection_prop['user'], connection_prop['passwd'],
                      connection_prop['host'], connection_prop['db'])
except DatabaseError:
    print("connection error")

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

# Ausprobierroute
@app.route("/testdb", methods=['GET', 'POST'])
def testdb():
    title = "Datenbankinhalte darstellen"
    # Get Data from DB
    data = dbNav.get_data_from_db_json('staedte_de_tiny')
    return data

# Ausprobierroute zu Forms mit Daten
@app.route("/putinlistelements", methods=['GET', 'POST'])
def putinlistelements():
    title = "Datenbankinhalte darstellen"
    # Get Data from DB
    data = dbNav.get_data_from_db_json('staedte_de_tiny').to_dict('r')
    return render_template('putinlistelements.html',
                           title=title,
                           posts=data)

# Ausprobierroute mit Eingabe und Auswirkung ()
@app.route("/auswahl_reaktion", methods=['GET','POST'])
def auswahl_reaktion():
    title = "Auswahl mit Dropdown und Reaktion"
    # Get Data from DB
    data = dbNav.get_data_from_db_json('staedte_de_tiny').to_dict('r')
    return render_template('auswahl_reaktion.html',
                           title=title,
                           posts=data)


# Ausprobierroute mit variabler Unterseite
@app.route("/items/<item>")
def items(item):
    return '<h1>This is a Item Page. Item is: {}.'.format(item)


if __name__ == '__main__':

    app.run(debug=True)


'''
https://www.youtube.com/watch?v=BFQfVd0g9sU
https://pythonspot.com/flask-web-forms/
'''

