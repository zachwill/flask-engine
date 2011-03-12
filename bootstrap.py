"""
Google App Engine uses this file to run your Flask application.

The root directory is modified to include the `libs` folder,
where flask, jinja2, werkzeug, and other libraries are stored.
"""

import sys
import os
from wsgiref.handlers import CGIHandler
from utils import adjust_root_dir


def main():
    adjust_root_dir()
    from app import app
    CGIHandler().run(app)


if __name__ == '__main__':
    main()
