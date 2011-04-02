"""
WTForms Documentation:    http://wtforms.simplecodes.com/
Flask WTForms Patterns:   http://flask.pocoo.org/docs/patterns/wtforms/
Flask-WTF Documentation:  http://packages.python.org/Flask-WTF/

Forms for your application can be stored in this file.
"""

from flaskext.wtf import (Form, TextField, TextAreaField, SubmitField,
        Required, Email)


class TodoForm(Form):
    """Simple todo form."""
    todo = TextField(validators=[Required()])
    submit = SubmitField("add")


class EmailForm(Form):
    """Simple email form."""
    name = TextField("Your Name", validators=[Required()])
    recipient = TextField("Recipient's Email", validators=[Email()])
    email = TextField("Your Email", validators=[Email()])
    message = TextAreaField("Message", validators=[Required()])
    submit = SubmitField("Send Email")
