#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([4, 1, 3, 2]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -9, -3]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 3, -4, 2]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 3.2, 2.8]), 3.2)

    def test_string(self):
        self.assertEqual(max_integer("abcd"), "d")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["abc", "xyz", "hij"]), "xyz")


if __name__ == "__main__":
    unittest.main()
