"""Google App Engine uses this file to run your Flask application."""

from wsgiref.handlers import CGIHandler
from app import app


def main():
    CGIHandler().run(app)

if __name__ == '__main__':
    main()
