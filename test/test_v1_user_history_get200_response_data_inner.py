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

from shionstream_sdk.models.v1_user_history_get200_response_data_inner import V1UserHistoryGet200ResponseDataInner

class TestV1UserHistoryGet200ResponseDataInner(unittest.TestCase):
    """V1UserHistoryGet200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1UserHistoryGet200ResponseDataInner:
        """Test V1UserHistoryGet200ResponseDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1UserHistoryGet200ResponseDataInner`
        """
        model = V1UserHistoryGet200ResponseDataInner()
        if include_optional:
            return V1UserHistoryGet200ResponseDataInner(
                id = '',
                anime_id = '',
                episode_id = '',
                episode_number = 1.337,
                progress_percent = 1.337,
                duration_seconds = 1.337,
                progress_seconds = 1.337,
                last_watched_at = ''
            )
        else:
            return V1UserHistoryGet200ResponseDataInner(
                id = '',
                anime_id = '',
                episode_id = '',
                progress_percent = 1.337,
                duration_seconds = 1.337,
                progress_seconds = 1.337,
                last_watched_at = '',
        )
        """

    def testV1UserHistoryGet200ResponseDataInner(self):
        """Test V1UserHistoryGet200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
