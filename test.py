"""Run unittests in the `tests` directory."""

from utils import find_gae_sdk

find_gae_sdk()

import unittest2


def main():
    suite = unittest2.loader.TestLoader().discover('tests')
    unittest2.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()
