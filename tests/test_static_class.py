import os
import sys
import unittest

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)

from staticclass.static_class import StaticClass


class StaticClassTests(unittest.TestCase):
    """Tests for staticclass.static_class.StaticClass"""
    def test_new(self):
        self.assertEqual(1, ExperimentalStaticClass.to_become_a_static_method())
        self.assertEqual(2, ExperimentalStaticClass.obviously_static_method())


class ExperimentalStaticClass(StaticClass):
    """Test class used by StaticClassTests"""

    def to_become_a_static_method():
        return 1

    @staticmethod
    def obviously_static_method():
        return 2


if __name__ == '__main__':
    unittest.main()