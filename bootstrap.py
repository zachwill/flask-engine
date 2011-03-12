"""
Google App Engine uses this file to run your Flask application.

The root directory is modified to include the `libs` folder,
where flask, jinja2, werkzeug, and other libraries are stored.
"""

import sys
import os
from wsgiref.handlers import CGIHandler
from app import app


def main():
    CGIHandler().run(app)

if __name__ == '__main__':
    main()
