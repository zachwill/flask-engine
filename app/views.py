"""
This file is used for both the routing and logic of your
application.
"""
from flask import Flask, url_for, render_template, request, redirect
from app.models import Todo
from app.forms import TodoForm

app = Flask('app')


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
