"""
Handy utility functions -- mostly for adjusting the sys path and/or
finding the Google App Engine SDK.
"""
import sys
import os


def adjust_root_dir():
    """Find libraries that are kept in `libs` folder."""
    root_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(root_dir, 'libs'))


def find_gae_sdk():
    """
    Correct any ImportError caused from being unable to find Google App
    Engine's SDK. These normally occur when trying to run the application
    from the commandline and/or when testing.
    """
    adjust_root_dir()
    from gae_path.util import gae_sdk_path, add_gae_sdk_path
    add_gae_sdk_path()
    sys.path.append(gae_sdk_path() + "/lib/yaml/lib")
    sys.path.append(gae_sdk_path() + "/lib/fancy_urllib")
    sys.path.append(gae_sdk_path() + '/lib/webob')
