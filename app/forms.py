from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, TextAreaField, validators

class SaySomething(FlaskForm):
  author = TextField('Author')
  message = TextAreaField('Message', [validators.Required("Please say something nice! :)")])
  submit = SubmitField('Post!')
