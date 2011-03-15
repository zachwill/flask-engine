"""
WTForms Documentation:   http://wtforms.simplecodes.com/
Flask WTForms Patterns:  http://flask.pocoo.org/docs/patterns/wtforms/

Forms for your application can be stored in this file.
"""

from flaskext.wtf import Form, TextField, Required


class TodoForm(Form):
    """Simple todo form."""
    todo = TextField(validators=[Required()])
