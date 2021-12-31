from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_simple_captcha import CAPTCHA

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)

CAPTCHA = CAPTCHA(app.config['CAPTCHA_CONFIG'])
app = CAPTCHA.init_app(app)

from app import routes
