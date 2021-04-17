from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)


from app import routes
