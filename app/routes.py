from app import app, models, tracer
from flask import render_template, redirect, url_for, request, json
from app.forms import SaySomething

messages = list([])
@app.route("/", methods=['GET', 'POST'])
@app.route("/<action>", methods=['GET', 'POST'])
def home(action=None, messages=messages):
  say_something_form = SaySomething()

  with tracer.start_as_current_span("home") as t:
    app.logger.info('"path": ' + request.path + 
    ', "method": ' + request.method + 
    ', "trace_id": ' + str(t.context.trace_id) + 
    ', "span_id": ' + str(t.context.span_id))

    if action == 'reset':
      with tracer.start_as_current_span("home-reset") as t:
        messages.clear()
        app.logger.info('"data": {"data": "Cleared cache"}')
        return redirect(url_for('home'))

    if say_something_form.validate_on_submit():
      with tracer.start_as_current_span("home-form"):
        author = say_something_form.author.data
        message = say_something_form.message.data
        messages.append({'author':author, 'message':message})
        app.logger.info('"data": {"author": ' + author + ', "message": ' + message + '}, ' + '"path": ' + request.path + 
        ', "method": ' + request.method + 
        ', "trace_id": ' + str(t.context.trace_id) + 
        ', "span_id": ' + str(t.context.span_id))
        return redirect(url_for('home'))

  return render_template("home.j2", title="Home", form=say_something_form, messages=messages)
