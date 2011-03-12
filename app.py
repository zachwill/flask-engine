# Flask Documentation:      http://flask.pocoo.org/docs/
# Jinja2 Documentation:     http://jinja.pocoo.org/2/documentation/
# Werkzeug Documentation:   http://werkzeug.pocoo.org/documentation/
# Python Datastore API: http://code.google.com/appengine/docs/python/datastore/

from flask import Flask, url_for, render_template, request, redirect
from models import Todo

app = Flask(__name__)


@app.route('/')
def index():
    """Render our website's index page."""
    return render_template('index.html')


@app.route('/todo/')
def todo_list():
    """Simple todo page."""
    return render_template('todo.html', todos=Todo.all().order('-created_at'))


@app.route('/todo/add', methods=["POST"])
def add_todo():
    """Add a todo."""
    todo = Todo(text=request.form['text'])
    todo.save()
    return redirect(url_for('todo_list'))


@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 page."""
    return render_template('404.html'), 404
