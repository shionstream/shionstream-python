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

from shionstream_sdk.models.v1_anime_slug_episodes_get200_response_data_inner import V1AnimeSlugEpisodesGet200ResponseDataInner

class TestV1AnimeSlugEpisodesGet200ResponseDataInner(unittest.TestCase):
    """V1AnimeSlugEpisodesGet200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1AnimeSlugEpisodesGet200ResponseDataInner:
        """Test V1AnimeSlugEpisodesGet200ResponseDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1AnimeSlugEpisodesGet200ResponseDataInner`
        """
        model = V1AnimeSlugEpisodesGet200ResponseDataInner()
        if include_optional:
            return V1AnimeSlugEpisodesGet200ResponseDataInner(
                id = '',
                number = 1.337,
                title = '',
                duration_seconds = 1.337,
                thumbnail = '',
                air_date = '',
                status = '',
                views_count = 1.337,
                is_vip = True,
                created_at = ''
            )
        else:
            return V1AnimeSlugEpisodesGet200ResponseDataInner(
                id = '',
                number = 1.337,
                title = '',
                duration_seconds = 1.337,
                status = '',
                views_count = 1.337,
                is_vip = True,
                created_at = '',
        )
        """

    def testV1AnimeSlugEpisodesGet200ResponseDataInner(self):
        """Test V1AnimeSlugEpisodesGet200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
