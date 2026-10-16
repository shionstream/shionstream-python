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

from shionstream_sdk.models.v1_user_history_post_request import V1UserHistoryPostRequest

class TestV1UserHistoryPostRequest(unittest.TestCase):
    """V1UserHistoryPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1UserHistoryPostRequest:
        """Test V1UserHistoryPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1UserHistoryPostRequest`
        """
        model = V1UserHistoryPostRequest()
        if include_optional:
            return V1UserHistoryPostRequest(
                anime_id = '0',
                episode_id = '0',
                episode_number = 1.337,
                progress_percent = 0,
                duration_seconds = 0,
                progress_seconds = 0
            )
        else:
            return V1UserHistoryPostRequest(
                anime_id = '0',
                episode_id = '0',
        )
        """

    def testV1UserHistoryPostRequest(self):
        """Test V1UserHistoryPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
