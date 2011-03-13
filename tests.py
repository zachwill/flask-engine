#!/usr/bin/env python
"""
Easy setup to run unittests for your code.

The code is pretty straight-forward -- it allows you to pull in any
libraries you might have in the libs folder, and also appends the appropriate
GAE SDK path.

After writing your tests, you can then run this script from the commandline:
    cd path/to/your/app
    python tests.py

"""

import unittest
from utils import find_gae_sdk

find_gae_sdk()

# You can write your unittests just like normal below.

from app import app


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
        self.app = app

    def test_flaskext_babel(self):
        from flaskext.babel import Babel
        babel = Babel(self.app)


if __name__ == '__main__':
    unittest.main()
