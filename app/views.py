"""
Flask Module Docs:  http://flask.pocoo.org/docs/api/#flask.Module

This file is used for both the routing and logic of your
application.
"""
from flask import Module, url_for, render_template, request, redirect
from models import Todo
from forms import TodoForm

views = Module(__name__, 'views')


@views.route('/')
def index():
    """Render website's index page."""
    return render_template('index.html')


@views.route('/todo/')
def todo_list():
    """Simple todo page."""
    form = TodoForm()
    todos = Todo.all().order('-created_at')
    return render_template('todo.html', form=form,
            todos=todos)


@views.route('/todo/add', methods=["POST"])
def add_todo():
    """Add a todo."""
    form = TodoForm()
    if request.method == 'POST' and form.validate_on_submit():
        todo = Todo(text=form.todo.data)
        todo.save()
    else:
        return str(form.errors)
    return redirect(url_for('todo_list'))


@views.route('/qunit/')
def qunit():
    """Render a QUnit page for JavaScript tests."""
    return render_template('test_js.html')


@views.app_errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
