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

from shionstream_sdk.models.v1_comments_post_request import V1CommentsPostRequest

class TestV1CommentsPostRequest(unittest.TestCase):
    """V1CommentsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CommentsPostRequest:
        """Test V1CommentsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CommentsPostRequest`
        """
        model = V1CommentsPostRequest()
        if include_optional:
            return V1CommentsPostRequest(
                anime_id = '0',
                episode_id = '0',
                content = '0',
                parent_id = '',
                is_spoiler = True,
                guest_name = '',
                guest_email = ''
            )
        else:
            return V1CommentsPostRequest(
                anime_id = '0',
                episode_id = '0',
                content = '0',
        )
        """

    def testV1CommentsPostRequest(self):
        """Test V1CommentsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
