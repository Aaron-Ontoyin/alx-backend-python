#!/usr/bin/env python3
"""Test client Module"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized

GithubOrgClient = __import__("client").GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Github Org Client Test Class"""

    @parameterized.expand(["google", "abc"])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test Org"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test Public Repos URL property"""

        mock_payload = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
        }

        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_property:
            mock_property.return_value = mock_payload
            test_class = GithubOrgClient("test_org")
            self.assertEqual(
                test_class._public_repos_url, mock_payload["repos_url"]
            )
