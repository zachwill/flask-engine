"""
Flask Documentation:       http://flask.pocoo.org/docs/
Jinja2 Documentation:      http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:    http://werkzeug.pocoo.org/documentation/
GAE Python Documentation:  http://code.google.com/appengine/docs/python/

This file creates your application.
"""

# If you want to debug your application locally using Flask's
# builtin run method -- then you should uncomment the lines below
# and move the utils.py file into your app directory. This can be
# useful for debugging your application's logic, but note that you'll
# be unable to interact with App Engine's database.
#
#from utils import find_gae_sdk
#find_gae_sdk('../libs')

from flask import Flask
from views import views
import settings


def create_app():
    """
    Create your application. Files outside the app directory can import
    this function and use it to recreate your application -- both
    bootstrap.py and the test directory do this.
    """
    app = Flask(__name__)
    app.config.from_object(settings)
    app.register_module(views)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
