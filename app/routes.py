from app import app, models, db, forms, CAPTCHA
from flask import render_template, redirect, url_for, request, json, flash


@app.route("/", methods=['GET', 'POST'])
def home():
  say_something_form = forms.SaySomething()
  captcha = CAPTCHA.create()
  messages = models.Comment.query.with_entities(models.Comment.author, models.Comment.message, models.Comment.datetime)

  if request.method == 'GET':
    return render_template("home.j2", title="Home", form=say_something_form, messages=messages, subject_name=app.config['SUBJECT_NAME'], captcha=captcha, retain_author="", retain_message="")

  if request.method == 'POST':
    if say_something_form.validate_on_submit():
      c_hash = request.form.get('captcha-hash')
      c_text = request.form.get('captcha-text')
      author = say_something_form.author.data
      message = say_something_form.message.data

      if c_text == "" or CAPTCHA.verify(c_text, c_hash) == False:
        flash("Captcha Incorrect.")
      elif CAPTCHA.verify(c_text, c_hash):
        remote_addr = request.remote_addr
        comment = models.Comment(author=author, message=message, remote_addr=remote_addr)
        db.session.add(comment)
        try: 
          db.session.commit()
        except:
          flash("Something went wrong.")

    return render_template("home.j2", title="Home", form=say_something_form, messages=messages, subject_name=app.config['SUBJECT_NAME'], captcha=captcha, retain_author=author, retain_message=message)

@app.route("/login", methods=['GET', 'POST'])
def login():
  login_form = forms.Login()

  if login_form.validate_on_submit():
    username = login_form.username.data
    password = login_form.password.data
  
  return render_template("login.j2", title="Login", form=login_form, subject_name=app.config['SUBJECT_NAME']
  )
