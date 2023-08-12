import sqlalchemy
import jinja2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, text, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import MetaData

engine = create_engine("sqlite:///library.sqlite", echo=True)

with engine.connect() as conn:
    metadata_obj = MetaData()

    user_table = Table(
        "user_account",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("name", String(30)),
        Column("fullname", String),
    )

    address_table = Table(
        "address",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("user_id", ForeignKey("user_account.id"), nullable=False),
        Column("email_address", String, nullable=False),
    )

    metadata_obj.create_all(engine)
