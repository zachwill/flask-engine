"""Google App Engine uses this file to run your Flask application."""

from utils import adjust_sys_path

adjust_sys_path()

from wsgiref.handlers import CGIHandler
from app import app


def main():
    CGIHandler().run(app)

if __name__ == '__main__':
    main()
