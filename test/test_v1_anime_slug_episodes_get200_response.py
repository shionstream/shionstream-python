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

from shionstream_sdk.models.v1_anime_slug_episodes_get200_response import V1AnimeSlugEpisodesGet200Response

class TestV1AnimeSlugEpisodesGet200Response(unittest.TestCase):
    """V1AnimeSlugEpisodesGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1AnimeSlugEpisodesGet200Response:
        """Test V1AnimeSlugEpisodesGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1AnimeSlugEpisodesGet200Response`
        """
        model = V1AnimeSlugEpisodesGet200Response()
        if include_optional:
            return V1AnimeSlugEpisodesGet200Response(
                success = true,
                anime = shionstream_sdk.models._v1_anime__slug__episodes_get_200_response_anime._v1_anime__slug__episodes_get_200_response_anime(
                    id = '', 
                    slug = '', 
                    title_romaji = '', ),
                data = [
                    shionstream_sdk.models._v1_anime__slug__episodes_get_200_response_data_inner._v1_anime__slug__episodes_get_200_response_data_inner(
                        id = '', 
                        number = 1.337, 
                        title = '', 
                        duration_seconds = 1.337, 
                        thumbnail = '', 
                        air_date = '', 
                        status = '', 
                        views_count = 1.337, 
                        is_vip = True, 
                        created_at = '', )
                    ],
                pagination = shionstream_sdk.models._v1_anime_get_200_response_pagination._v1_anime_get_200_response_pagination(
                    page = 1.337, 
                    limit = 1.337, 
                    total = 1.337, 
                    total_pages = 1.337, )
            )
        else:
            return V1AnimeSlugEpisodesGet200Response(
                success = true,
                anime = shionstream_sdk.models._v1_anime__slug__episodes_get_200_response_anime._v1_anime__slug__episodes_get_200_response_anime(
                    id = '', 
                    slug = '', 
                    title_romaji = '', ),
                data = [
                    shionstream_sdk.models._v1_anime__slug__episodes_get_200_response_data_inner._v1_anime__slug__episodes_get_200_response_data_inner(
                        id = '', 
                        number = 1.337, 
                        title = '', 
                        duration_seconds = 1.337, 
                        thumbnail = '', 
                        air_date = '', 
                        status = '', 
                        views_count = 1.337, 
                        is_vip = True, 
                        created_at = '', )
                    ],
                pagination = shionstream_sdk.models._v1_anime_get_200_response_pagination._v1_anime_get_200_response_pagination(
                    page = 1.337, 
                    limit = 1.337, 
                    total = 1.337, 
                    total_pages = 1.337, ),
        )
        """

    def testV1AnimeSlugEpisodesGet200Response(self):
        """Test V1AnimeSlugEpisodesGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
