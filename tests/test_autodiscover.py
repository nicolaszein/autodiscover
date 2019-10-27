import sys
import unittest
import pathlib

from autodiscover import AutoDiscover

PATH = 'tests/module_to_import'


class TestAutoDiscover(unittest.TestCase):

    def test_autodiscover(self):
        path = pathlib.Path(PATH)
        autodiscover = AutoDiscover(path=path)
        module = 'tests.module_to_import'
        self.assertNotIn(module, sys.modules)

        autodiscover()

        self.assertIn(module, sys.modules)

    def test_autodiscover_with_pattern(self):
        path = pathlib.Path(PATH)
        autodiscover = AutoDiscover(path=path, pattern='pattern.py')
        module = 'tests.module_to_import.pattern'
        sys.modules.pop(module)

        autodiscover()

        self.assertIn(module, sys.modules)
