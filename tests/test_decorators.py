import os
import sys
import unittest

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)

from staticclass.decorators import not_static
from staticclass.static_class import StaticClass


class NotStaticTests(unittest.TestCase):
    """Tests for staticclass.decorators.not_static"""

    def test_not_static(self):
        self.assertEqual(1, ExperimentalStaticClass.static_method())
        self.assertEqual(2, ExperimentalStaticClass().not_static_method())


class ExperimentalStaticClass(StaticClass):
    """Test class for NoStaticTests"""

    def static_method():
        return 1

    @not_static
    def not_static_method(self):
        return 2


if __name__ == '__main__':
    unittest.main()