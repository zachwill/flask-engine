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
