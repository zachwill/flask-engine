"""
Flask Documentation:       http://flask.pocoo.org/docs/
Jinja2 Documentation:      http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:    http://werkzeug.pocoo.org/documentation/
GAE Python Documentation:  http://code.google.com/appengine/docs/python/

The `apps.py` file is used for both the routing and logic of your
application by default, but this can be split apart similar to how
Django splits models, views, urls, and templates.
"""
from utils import adjust_root_dir
from models import Todo

adjust_root_dir()

from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    """Render website's index page."""
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
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


@app.route('/qunit/')
def qunit():
    """Render a QUnit page for JavaScript tests."""
    return render_template('test_js.html')
