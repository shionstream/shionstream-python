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

from shionstream_sdk.models.v1_anime_slug_episodes_get200_response_anime import V1AnimeSlugEpisodesGet200ResponseAnime

class TestV1AnimeSlugEpisodesGet200ResponseAnime(unittest.TestCase):
    """V1AnimeSlugEpisodesGet200ResponseAnime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1AnimeSlugEpisodesGet200ResponseAnime:
        """Test V1AnimeSlugEpisodesGet200ResponseAnime
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1AnimeSlugEpisodesGet200ResponseAnime`
        """
        model = V1AnimeSlugEpisodesGet200ResponseAnime()
        if include_optional:
            return V1AnimeSlugEpisodesGet200ResponseAnime(
                id = '',
                slug = '',
                title_romaji = ''
            )
        else:
            return V1AnimeSlugEpisodesGet200ResponseAnime(
                id = '',
                slug = '',
                title_romaji = '',
        )
        """

    def testV1AnimeSlugEpisodesGet200ResponseAnime(self):
        """Test V1AnimeSlugEpisodesGet200ResponseAnime"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
