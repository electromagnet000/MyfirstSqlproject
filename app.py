import sqlalchemy
import jinja2
from flask import Flask, render_template, request, redirect, url_for, session, g, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, text, ForeignKey, insert, select, func
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import MetaData


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/library.sqlite'

engine = create_engine('sqlite:///library.sqlite')
Base = declarative_base()



@app.route("/add_author", methods=['GET, POST'])
def add_author():
    if request.method == 'POST':
        pass
    return render_template("add_author.html")




