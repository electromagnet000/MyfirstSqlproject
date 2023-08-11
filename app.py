import sqlalchemy
import jinja2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('sqlite:///library.sqlite', echo=True)

stmt = text("SELECT x, y FROM Authors WHERE y > :y ORDER BY x, y")
with Session(engine) as session:
    result = session.execute(stmt, {"y": 6})
    for row in result:
        print(f"x")