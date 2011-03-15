"""
Using gaeunit.py to run tests -- while tests can't be run from the
commandline, this is currently the best way I've found to use the Python
unittest module.
"""
import unittest
from utils import adjust_sys_path

adjust_sys_path()

# You can write your unittests just like normal below.

from app import create_app


class LibsImportTest(unittest.TestCase):

    def setUp(self):
        import libs.flask
        self.path = libs.flask.__path__

    def test_regular_import_without_lib(self):
        import flask
        path = flask.__path__
        self.assertEquals(path, self.path)

    def test_from_libs_import(self):
        from libs import flask
        path = flask.__path__
        self.assertEquals(path, self.path)

    def test_import_flaskext(self):
        import flaskext


class AppTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()


if __name__ == '__main__':
    unittest.main()
