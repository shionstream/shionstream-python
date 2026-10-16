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

from shionstream_sdk.models.v1_comments_id_like_post200_response import V1CommentsIdLikePost200Response

class TestV1CommentsIdLikePost200Response(unittest.TestCase):
    """V1CommentsIdLikePost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CommentsIdLikePost200Response:
        """Test V1CommentsIdLikePost200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CommentsIdLikePost200Response`
        """
        model = V1CommentsIdLikePost200Response()
        if include_optional:
            return V1CommentsIdLikePost200Response(
                success = true,
                message = ''
            )
        else:
            return V1CommentsIdLikePost200Response(
                success = true,
                message = '',
        )
        """

    def testV1CommentsIdLikePost200Response(self):
        """Test V1CommentsIdLikePost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
