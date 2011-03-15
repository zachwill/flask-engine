"""Google App Engine uses this file to run your Flask application."""

from utils import adjust_sys_path

adjust_sys_path()

from wsgiref.handlers import CGIHandler
from app import create_app


def main():
    app = create_app()
    CGIHandler().run(app)

if __name__ == '__main__':
    main()
