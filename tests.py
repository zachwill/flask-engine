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

from utils import find_gae_sdk

find_gae_sdk()

# You can write your unittests just like normal below.


import unittest
from app import app


class AppTest(unittest.TestCase):

    def setUp(self):
        self.app = app

    def test_pass(self):
        pass

    def test_import_from_libs_folder(self):
        import flask


if __name__ == '__main__':
    unittest.main()
