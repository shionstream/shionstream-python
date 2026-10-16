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

from shionstream_sdk.api.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()

    def tearDown(self) -> None:
        pass

    def test_v1_user_history_delete(self) -> None:
        """Test case for v1_user_history_delete

        Clear All History
        """
        pass

    def test_v1_user_history_get(self) -> None:
        """Test case for v1_user_history_get

        Get Watch History
        """
        pass

    def test_v1_user_history_id_delete(self) -> None:
        """Test case for v1_user_history_id_delete

        Delete History Item
        """
        pass

    def test_v1_user_history_post(self) -> None:
        """Test case for v1_user_history_post

        Record Playback Progress
        """
        pass

    def test_v1_user_profile_get(self) -> None:
        """Test case for v1_user_profile_get

        Get User Profile
        """
        pass

    def test_v1_user_settings_get(self) -> None:
        """Test case for v1_user_settings_get

        Get User Settings
        """
        pass

    def test_v1_user_settings_patch(self) -> None:
        """Test case for v1_user_settings_patch

        Update User Settings
        """
        pass

    def test_v1_user_watchlist_anime_id_delete(self) -> None:
        """Test case for v1_user_watchlist_anime_id_delete

        Remove from Watchlist
        """
        pass

    def test_v1_user_watchlist_anime_id_patch(self) -> None:
        """Test case for v1_user_watchlist_anime_id_patch

        Update Watchlist Entry
        """
        pass

    def test_v1_user_watchlist_get(self) -> None:
        """Test case for v1_user_watchlist_get

        Get User Watchlist
        """
        pass

    def test_v1_user_watchlist_post(self) -> None:
        """Test case for v1_user_watchlist_post

        Add to Watchlist
        """
        pass


if __name__ == '__main__':
    unittest.main()
