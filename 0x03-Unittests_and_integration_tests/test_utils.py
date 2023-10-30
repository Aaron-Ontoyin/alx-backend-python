#!/usr/bin/env python3
"""Test utils Module"""


import unittest
from parameterized import parameterized

utils = __import__('utils')


class TestAccessNestedMap(unittest.TestCase):
    """Access Map Test Class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test Access Nested Map"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test Access Nested Map Exception"""
        with self.assertRaises(expected):
            utils.access_nested_map(nested_map, path)
