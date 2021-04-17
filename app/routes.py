from app import app, models, db
from flask import render_template, redirect, url_for, request, json, flash
from app.forms import SaySomething

@app.route("/", methods=['GET', 'POST'])
@app.route("/<action>", methods=['GET', 'POST'])
def home():
  say_something_form = SaySomething()

  if say_something_form.validate_on_submit():
    author = say_something_form.author.data
    message = say_something_form.message.data
    remote_addr = request.remote_addr
    
    comment = models.Comment(author=author, message=message, remote_addr=remote_addr)
    db.session.add(comment)
    try: 
      db.session.commit()
    except:
      flash("Something went wrong. Is your message too long?")
    return redirect(url_for('home'))
  
  messages = models.Comment.query.with_entities(models.Comment.author, models.Comment.message, models.Comment.datetime)
  return render_template("home.j2", title="Home", form=say_something_form, messages=messages, subject_name=app.config['SUBJECT_NAME'])
