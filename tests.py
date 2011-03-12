#!/usr/bin/python

"""
Easy setup to run unittests for your code.

The code is pretty straight-forward -- it allows you to pull in any
libraries you might have in the libs folder, then appends the appropriate
GAE SDK path.

After writing your tests, you can then run this script from the commandline:
    cd path/to/your/app
    python tests.py

"""


import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT_DIR, 'libs'))

from gae_path.util import gae_sdk_path, add_gae_sdk_path

add_gae_sdk_path()
sys.path.append(gae_sdk_path() + "/lib/yaml/lib")
sys.path.append(gae_sdk_path() + "/lib/fancy_urllib")
sys.path.append(gae_sdk_path() + '/lib/webob')


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
