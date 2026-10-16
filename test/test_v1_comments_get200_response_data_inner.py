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

from shionstream_sdk.models.v1_comments_get200_response_data_inner import V1CommentsGet200ResponseDataInner

class TestV1CommentsGet200ResponseDataInner(unittest.TestCase):
    """V1CommentsGet200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CommentsGet200ResponseDataInner:
        """Test V1CommentsGet200ResponseDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CommentsGet200ResponseDataInner`
        """
        model = V1CommentsGet200ResponseDataInner()
        if include_optional:
            return V1CommentsGet200ResponseDataInner(
                id = '',
                anime_id = '',
                episode_id = '',
                user_id = '',
                guest_name = '',
                parent_id = '',
                content = '',
                is_spoiler = True,
                created_at = '',
                updated_at = '',
                likes = 1.337,
                dislikes = 1.337
            )
        else:
            return V1CommentsGet200ResponseDataInner(
                id = '',
                anime_id = '',
                episode_id = '',
                content = '',
                is_spoiler = True,
                created_at = '',
                updated_at = '',
                likes = 1.337,
                dislikes = 1.337,
        )
        """

    def testV1CommentsGet200ResponseDataInner(self):
        """Test V1CommentsGet200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
