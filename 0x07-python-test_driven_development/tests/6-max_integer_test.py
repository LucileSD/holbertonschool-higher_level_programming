#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        tests for max_integer function
    """
    def test_is_integer(self):
        """
            checks if values are integers
        """
        self.assertEqual(max_integer([1, 2, 3, 5, 4]), 5)
        self.assertEqual(max_integer([-2, -6, -1, -12]), -1)
        self.assertEqual(max_integer([1, 266, 3, 3605]), 3605)

    def test_is_float(self):
        """
            checks if values are floats
        """
        self.assertEqual(max_integer([1.2, 6.63, 6.6, 1.24]), 6.63)
        self.assertEqual(max_integer([12.1, 12.14, 12.16]), 12.16)
        self.assertEqual(max_integer([2, 2.1, 2.20, 2.22]), 2.22)

    def test_is_string(self):
        """
            checks if values are strings
        """
        self.assertEqual(max_integer("Hello"), "o")
        self.assertEqual(max_integer(["a", "string", "hello"]), "string")

    def test_is_none(self):
        """
            checks if nothing is given
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()
