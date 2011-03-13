"""Additional sample test file that will run along with app_tests.py"""

import unittest
from google.appengine.api import urlfetch


class AppEngineAPITest(unittest.TestCase):

    def test_urlfetch(self):
        response = urlfetch.fetch('http://www.google.com')
        self.assertTrue(response.content.find('<html>'))

