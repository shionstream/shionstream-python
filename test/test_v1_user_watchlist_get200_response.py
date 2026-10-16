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

from shionstream_sdk.models.v1_user_watchlist_get200_response import V1UserWatchlistGet200Response

class TestV1UserWatchlistGet200Response(unittest.TestCase):
    """V1UserWatchlistGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1UserWatchlistGet200Response:
        """Test V1UserWatchlistGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1UserWatchlistGet200Response`
        """
        model = V1UserWatchlistGet200Response()
        if include_optional:
            return V1UserWatchlistGet200Response(
                success = true,
                data = [
                    shionstream_sdk.models._v1_user_watchlist_get_200_response_data_inner._v1_user_watchlist_get_200_response_data_inner(
                        id = '', 
                        anime_id = '', 
                        status = '', 
                        is_favorite = True, 
                        current_episode = 1.337, 
                        user_rating = 1.337, 
                        created_at = '', 
                        updated_at = '', )
                    ]
            )
        else:
            return V1UserWatchlistGet200Response(
                success = true,
                data = [
                    shionstream_sdk.models._v1_user_watchlist_get_200_response_data_inner._v1_user_watchlist_get_200_response_data_inner(
                        id = '', 
                        anime_id = '', 
                        status = '', 
                        is_favorite = True, 
                        current_episode = 1.337, 
                        user_rating = 1.337, 
                        created_at = '', 
                        updated_at = '', )
                    ],
        )
        """

    def testV1UserWatchlistGet200Response(self):
        """Test V1UserWatchlistGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
