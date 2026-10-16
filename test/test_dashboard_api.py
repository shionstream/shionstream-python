# coding: utf-8

"""
    ShionStream API

    Modular anime streaming and metadata API built with Hono on Cloudflare Workers.

    The version of the OpenAPI document: 1.0.0
    Author: ShionStream Engineering Team
    Contact: dev@gox.my.id
    Website: https://gox.my.id

    Generated for ShionStream API SDK.
    Do not edit the class manually.
"""  # noqa: E501


import unittest

from shionstream_sdk.api.dashboard_api import DashboardApi


class TestDashboardApi(unittest.TestCase):
    """DashboardApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DashboardApi()

    def tearDown(self) -> None:
        pass

    def test_v1_dashboard_anime_get(self) -> None:
        """Test case for v1_dashboard_anime_get

        Get Administrative Anime List
        """
        pass

    def test_v1_dashboard_categories_get(self) -> None:
        """Test case for v1_dashboard_categories_get

        Get Category & Genre Distributions
        """
        pass

    def test_v1_dashboard_episodes_get(self) -> None:
        """Test case for v1_dashboard_episodes_get

        Get Administrative Episodes List
        """
        pass

    def test_v1_dashboard_moderation_get(self) -> None:
        """Test case for v1_dashboard_moderation_get

        Get Comment Moderation Reports
        """
        pass

    def test_v1_dashboard_moderation_id_patch(self) -> None:
        """Test case for v1_dashboard_moderation_id_patch

        Resolve or Dismiss Moderation Report
        """
        pass

    def test_v1_dashboard_overview_get(self) -> None:
        """Test case for v1_dashboard_overview_get

        Get Dashboard Overview
        """
        pass

    def test_v1_dashboard_roles_get(self) -> None:
        """Test case for v1_dashboard_roles_get

        Get System Roles & Permissions
        """
        pass

    def test_v1_dashboard_seasons_get(self) -> None:
        """Test case for v1_dashboard_seasons_get

        Get Seasonal Broadcast Distributions
        """
        pass

    def test_v1_dashboard_stats_get(self) -> None:
        """Test case for v1_dashboard_stats_get

        Get Platform Stats
        """
        pass

    def test_v1_dashboard_users_get(self) -> None:
        """Test case for v1_dashboard_users_get

        Get Users Directory (Admin Only)
        """
        pass


if __name__ == '__main__':
    unittest.main()
