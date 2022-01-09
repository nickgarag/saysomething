import datetime
from app import db

class Comment(db.Model):
  __tablename__ = 'comment'
  id = db.Column(db.Integer, primary_key=True)
  author = db.Column(db.String(126), unique=False, nullable=True, default="Anonymous")
  message = db.Column(db.String(3000), unique=False, nullable=True)
  remote_addr = db.Column(db.String(20), unique=False, nullable=True)
  datetime = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

#Seems to be the easier option for creating tables that dont exist.
db.create_all()
