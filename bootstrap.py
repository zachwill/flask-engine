"""
Google App Engine uses this file to run your Flask application.

The root directory is modified to include the `libs` folder,
where flask, jinja2, werkzeug, and other libraries are stored.
"""

import sys
import os

# Let's keep flask, jinja2, and werkzeug in a separate libs folder.
# NOTE: You can add other libraries here, too -- and still
# import them as normal.

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT_DIR, 'libs'))

from wsgiref.handlers import CGIHandler
from app import app
CGIHandler().run(app)
