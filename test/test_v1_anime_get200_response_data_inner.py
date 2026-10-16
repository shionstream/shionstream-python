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

from shionstream_sdk.models.v1_anime_get200_response_data_inner import V1AnimeGet200ResponseDataInner

class TestV1AnimeGet200ResponseDataInner(unittest.TestCase):
    """V1AnimeGet200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1AnimeGet200ResponseDataInner:
        """Test V1AnimeGet200ResponseDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1AnimeGet200ResponseDataInner`
        """
        model = V1AnimeGet200ResponseDataInner()
        if include_optional:
            return V1AnimeGet200ResponseDataInner(
                id = '',
                slug = '',
                title_romaji = '',
                title_english = '',
                title_japanese = '',
                synopsis = '',
                cover_image = '',
                banner_image = '',
                type = '',
                status = '',
                season_name = '',
                season_year = 1.337,
                episodes_count = 1.337,
                duration_per_ep = '',
                rating = 1.337,
                is_featured = True,
                is_trending = True,
                sub_or_dub = ''
            )
        else:
            return V1AnimeGet200ResponseDataInner(
                id = '',
                slug = '',
                title_romaji = '',
                type = '',
                status = '',
                episodes_count = 1.337,
                is_featured = True,
                is_trending = True,
                sub_or_dub = '',
        )
        """

    def testV1AnimeGet200ResponseDataInner(self):
        """Test V1AnimeGet200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
