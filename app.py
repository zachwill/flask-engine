"""
Flask Documentation:       http://flask.pocoo.org/docs/
Jinja2 Documentation:      http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:    http://werkzeug.pocoo.org/documentation/
GAE Python Documentation:  http://code.google.com/appengine/docs/python/

This file is used for both the routing and logic of your
application by default, but it can be split apart similar to how
Django splits views and urls into separate files.

NOTE: If you're wanting to use reCaptcha support for your application,
you will have to obtain keys from http://recaptcha.net/ -- the keys
provided here will only work while you're developing on localhost.
"""
from utils import adjust_sys_path
from models import Todo

adjust_sys_path()

# You can now import from libs like normal.

from flask import Flask, url_for, render_template, request, redirect
from wtforms import Form, TextField, validators

app = Flask(__name__)
app.debug = True


class TodoForm(Form):
    """Simple todo form."""
    todo = TextField([validators.Required()])


@app.route('/')
def index():
    """Render website's index page."""
    return render_template('index.html')


@app.route('/todo/')
def todo_list():
    """Simple todo page."""
    form = TodoForm()
    return render_template('todo.html', form=form,
            todos=Todo.all().order('-created_at'))


@app.route('/todo/add', methods=["POST"])
def add_todo():
    """Add a todo."""
    form = TodoForm(request.form)
    if request.method == 'POST' and form.validate():
        todo = Todo(text=form.todo.data)
        todo.save()
    return redirect(url_for('todo_list'))


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


@app.route('/qunit/')
def qunit():
    """Render a QUnit page for JavaScript tests."""
    return render_template('test_js.html')
