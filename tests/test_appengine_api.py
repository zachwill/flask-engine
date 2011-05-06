"""Additional sample test file that will run along with test_app.py"""

import unittest
from google.appengine.ext import testbed
from google.appengine.api import urlfetch


class AppEngineAPITest(unittest.TestCase):

    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Initialize urlfetch stub.
        self.testbed.init_urlfetch_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_urlfetch(self):
        response = urlfetch.fetch('http://www.google.com')
        self.assertTrue(response.content.find('<html>'))
