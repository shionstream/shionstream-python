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

from shionstream_sdk.api.episodes_api import EpisodesApi


class TestEpisodesApi(unittest.TestCase):
    """EpisodesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EpisodesApi()

    def tearDown(self) -> None:
        pass

    def test_v1_anime_slug_episodes_get(self) -> None:
        """Test case for v1_anime_slug_episodes_get

        List Episodes by Anime Slug
        """
        pass

    def test_v1_episodes_id_stream_get(self) -> None:
        """Test case for v1_episodes_id_stream_get

        Get Episode Stream Sources
        """
        pass


if __name__ == '__main__':
    unittest.main()
