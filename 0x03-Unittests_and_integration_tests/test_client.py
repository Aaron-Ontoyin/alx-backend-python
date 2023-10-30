#!/usr/bin/env python3
"""Test client Module"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Github Org Client Test Class"""

    @parameterized.expand(["google", "abc"])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test Org"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
