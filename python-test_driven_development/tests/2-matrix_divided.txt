#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    TestCase for the max_integer function to find the maximum
    integer in a list.
    """

    def test_ordered_list(self):
        """Test with an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with the maximum value at the beginning."""
        self.assertEqual(max_integer([10, 5, 2]), 10)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        """Test with a single element in the list."""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.53, 6.33, -9.12, 15.6]), 15.6)

    def test_list_of_strings(self):
        """Test with a list of strings."""
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")

    def test_negative_numbers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -5, -10, -2]), -1)


if __name__ == '__main__':
    unittest.main()
