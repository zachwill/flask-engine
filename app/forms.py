"""
WTForms Documentation:   http://wtforms.simplecodes.com/
Flask WTForms Patterns:  http://flask.pocoo.org/docs/patterns/wtforms/

Forms for your application can be stored in this file.
"""

from wtforms import Form, TextField, validators


class TodoForm(Form):
    """Simple todo form."""
    todo = TextField([validators.Required()])
