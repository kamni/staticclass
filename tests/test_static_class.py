import os
import sys
import unittest

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)

from staticclass.static_class import StaticClass, StaticMetaClass


class StaticMetaClassTests(unittest.TestCase):
    """Tests for staticclass.static_class.StaticMetaClass"""

    def test_can_be_static__default(self):
        attr_name = 'foo'
        attr = lambda x: x
        self.assertTrue(StaticMetaClass._can_be_static(attr_name, attr))

    def test_can_be_static__has_notstatic_attr_but_not_protected(self):
        attr_name = 'foo'
        attr = lambda x: x
        attr.__nostatic__ = False
        self.assertTrue(StaticMetaClass._can_be_static(attr_name, attr))

    def test_can_be_static__must_be_a_function(self):
        attr_name = 'foo'
        # we want to avoid things like classes that are simply callable
        attr = type('foo', (object,), {})
        self.assertFalse(StaticMetaClass._can_be_static(attr_name, attr))

    def test_can_be_static__must_not_be_a_dunderscore_method(self):
        attr_name = '__foo__'
        attr = lambda x: x
        self.assertFalse(StaticMetaClass._can_be_static(attr_name, attr))

    def test_can_be_static__must_not_be_protected_from_static(self):
        attr_name = '__foo__'
        attr = lambda x: x
        attr.__nostatic__ = True
        self.assertFalse(StaticMetaClass._can_be_static(attr_name, attr))


class StaticClassTests(unittest.TestCase):
    """Tests for staticclass.static_class.StaticClass"""

    def test_new__creates_static_methods(self):
        self.assertEqual(1, ExperimentalStaticClass.to_become_a_static_method())

    def test_new__still_handles_decorated_static_methods(self):
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