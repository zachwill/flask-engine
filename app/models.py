"""
Python Datastore API: http://code.google.com/appengine/docs/python/datastore/
"""

from google.appengine.ext import db


class Todo(db.Model):
    text = db.StringProperty()
    created_at = db.DateTimeProperty(auto_now=True)
