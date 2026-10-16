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

from shionstream_sdk.models.v1_user_watchlist_anime_id_patch_request import V1UserWatchlistAnimeIdPatchRequest

class TestV1UserWatchlistAnimeIdPatchRequest(unittest.TestCase):
    """V1UserWatchlistAnimeIdPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1UserWatchlistAnimeIdPatchRequest:
        """Test V1UserWatchlistAnimeIdPatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1UserWatchlistAnimeIdPatchRequest`
        """
        model = V1UserWatchlistAnimeIdPatchRequest()
        if include_optional:
            return V1UserWatchlistAnimeIdPatchRequest(
                status = '',
                is_favorite = True
            )
        else:
            return V1UserWatchlistAnimeIdPatchRequest(
        )
        """

    def testV1UserWatchlistAnimeIdPatchRequest(self):
        """Test V1UserWatchlistAnimeIdPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
