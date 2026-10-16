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

from shionstream_sdk.api.anime_api import AnimeApi


class TestAnimeApi(unittest.TestCase):
    """AnimeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AnimeApi()

    def tearDown(self) -> None:
        pass

    def test_v1_anime_get(self) -> None:
        """Test case for v1_anime_get

        List Anime Catalog
        """
        pass

    def test_v1_anime_slug_get(self) -> None:
        """Test case for v1_anime_slug_get

        Get Anime Details by Slug
        """
        pass


if __name__ == '__main__':
    unittest.main()
