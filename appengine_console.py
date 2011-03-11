#!/usr/bin/python

"""
For more information on the remote api:
    http://code.google.com/appengine/articles/remote_api.html

How do you use this?
    python appengine_console.py <your_app_name_here>
"""

import code
import getpass
import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT_DIR, 'libs'))

from gae_path.util import gae_sdk_path, add_gae_sdk_path

add_gae_sdk_path()
sys.path.append(gae_sdk_path() + "/lib/yaml/lib")
sys.path.append(gae_sdk_path() + "/lib/fancy_urllib")
sys.path.append(gae_sdk_path() + '/lib/webob')

from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.ext import db

def auth_func():
    return raw_input('Username:'), getpass.getpass('Password:')

if len(sys.argv) < 2:
    print "Usage: %s app_id [host]" % (sys.argv[0],)
app_id = sys.argv[1]
if len(sys.argv) > 2:
    host = sys.argv[2]
else:
    host = '%s.appspot.com' % app_id

remote_api_stub.ConfigureRemoteDatastore(app_id, '/remote_api', auth_func, host)

code.interact('App Engine interactive console for %s' % (app_id,), None, locals())

