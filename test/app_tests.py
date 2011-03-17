"""
Using gaeunit.py to run tests -- while tests can't be run from the
commandline, this is currently the best way I've found to use the Python
unittest module.
"""

import unittest
from utils import adjust_sys_path

adjust_sys_path()

# And just write your unittests like normal below.

import flask


class LibsImportTest(unittest.TestCase):

    def setUp(self):
        import libs.flask
        self.path = libs.flask.__path__

    def test_regular_path_without_libs(self):
        flask_path = flask.__path__
        assert flask_path == self.path


class AppTest(unittest.TestCase):

    def setUp(self):
        from app import create_app
        app = create_app()
        self.app = app.test_client()

    def test_index_page(self):
        rv = self.app.get('/')
        assert "I'm in yo app-engine" in rv.data

    def test_flask_default_redirecting(self):
        rv = self.app.get('/todo')
        assert 'Redirecting' in rv.data
        assert rv.status_code == 301

    def test_todo_page(self):
        rv = self.app.get('/todo/')
        assert 'some todos' in rv.data

    def test_add_todo_csrf_is_missing(self):
        rv = self.app.post('/todo/add', flask.json.dumps({'todo':'tests'}))
        assert 'Missing or invalid CSRF token' in rv.data

    def test_qunit_page(self):
        rv = self.app.get('/qunit/')
        assert 'QUnit Tests' in rv.data

    def test_404_page(self):
        rv = self.app.get('/i-am-not-found/')
        assert rv.status_code == 404


if __name__ == '__main__':
    unittest.main()
