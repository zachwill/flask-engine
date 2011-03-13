"""
Flask Documentation:       http://flask.pocoo.org/docs/
Jinja2 Documentation:      http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:    http://werkzeug.pocoo.org/documentation/
GAE Python Documentation:  http://code.google.com/appengine/docs/python/

This file initializes your application.
"""

from flask import Flask, url_for, render_template, request, redirect
from wtforms import Form, TextField, validators
from models import Todo

app = Flask('app')
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


@app.route('/qunit/')
def qunit():
    """Render a QUnit page for JavaScript tests."""
    return render_template('test_js.html')


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
