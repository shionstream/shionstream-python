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

from shionstream_sdk.models.v1_anime_slug_get200_response import V1AnimeSlugGet200Response

class TestV1AnimeSlugGet200Response(unittest.TestCase):
    """V1AnimeSlugGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1AnimeSlugGet200Response:
        """Test V1AnimeSlugGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1AnimeSlugGet200Response`
        """
        model = V1AnimeSlugGet200Response()
        if include_optional:
            return V1AnimeSlugGet200Response(
                success = true,
                data = shionstream_sdk.models._v1_anime__slug__get_200_response_data._v1_anime__slug__get_200_response_data(
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
                    sub_or_dub = '', 
                    genres = [
                        shionstream_sdk.models._v1_anime__slug__get_200_response_data_genres_inner._v1_anime__slug__get_200_response_data_genres_inner(
                            id = '', 
                            name = '', 
                            slug = '', )
                        ], 
                    studios = [
                        shionstream_sdk.models._v1_anime__slug__get_200_response_data_genres_inner._v1_anime__slug__get_200_response_data_genres_inner(
                            id = '', 
                            name = '', 
                            slug = '', )
                        ], 
                    schedule = shionstream_sdk.models._v1_anime__slug__get_200_response_data_schedule._v1_anime__slug__get_200_response_data_schedule(
                        release_day = '', 
                        release_time = '', 
                        episode_number = 1.337, 
                        status = '', 
                        timezone = '', ), 
                    trending_stats = shionstream_sdk.models._v1_anime__slug__get_200_response_data_trending_stats._v1_anime__slug__get_200_response_data_trendingStats(
                        rank = 1.337, 
                        trend_score = 1.337, 
                        total_views = 1.337, ), )
            )
        else:
            return V1AnimeSlugGet200Response(
                success = true,
                data = shionstream_sdk.models._v1_anime__slug__get_200_response_data._v1_anime__slug__get_200_response_data(
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
                    sub_or_dub = '', 
                    genres = [
                        shionstream_sdk.models._v1_anime__slug__get_200_response_data_genres_inner._v1_anime__slug__get_200_response_data_genres_inner(
                            id = '', 
                            name = '', 
                            slug = '', )
                        ], 
                    studios = [
                        shionstream_sdk.models._v1_anime__slug__get_200_response_data_genres_inner._v1_anime__slug__get_200_response_data_genres_inner(
                            id = '', 
                            name = '', 
                            slug = '', )
                        ], 
                    schedule = shionstream_sdk.models._v1_anime__slug__get_200_response_data_schedule._v1_anime__slug__get_200_response_data_schedule(
                        release_day = '', 
                        release_time = '', 
                        episode_number = 1.337, 
                        status = '', 
                        timezone = '', ), 
                    trending_stats = shionstream_sdk.models._v1_anime__slug__get_200_response_data_trending_stats._v1_anime__slug__get_200_response_data_trendingStats(
                        rank = 1.337, 
                        trend_score = 1.337, 
                        total_views = 1.337, ), ),
        )
        """

    def testV1AnimeSlugGet200Response(self):
        """Test V1AnimeSlugGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
