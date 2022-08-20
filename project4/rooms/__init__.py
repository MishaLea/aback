import os
import re
from flask import Flask
from flask_sqlalchemy import flask_sqlalchemy
if os.path.exists("env.py"):
    import env 


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri = uri.replace("postgres://", "postgrsql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

db = flask_SQLAlchemy(app)

from taskmanager import routes #noqa 