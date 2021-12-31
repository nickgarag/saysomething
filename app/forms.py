from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, TextAreaField, validators

class SaySomething(FlaskForm):
  author = TextField('Author')
  message = TextAreaField('Message', [validators.Required("Please say something nice! :)")])
  submit = SubmitField('Post!')

class Login(FlaskForm):
  username = TextField('Username', [validators.Required("Username required"), validators.Length(min=4, max=32)])
  password = TextField('Password', [validators.Required("Password required"), validators.Length(min=16, max=128)])