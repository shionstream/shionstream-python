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

from shionstream_sdk.models.v1_comments_get200_response import V1CommentsGet200Response

class TestV1CommentsGet200Response(unittest.TestCase):
    """V1CommentsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CommentsGet200Response:
        """Test V1CommentsGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CommentsGet200Response`
        """
        model = V1CommentsGet200Response()
        if include_optional:
            return V1CommentsGet200Response(
                success = true,
                data = [
                    shionstream_sdk.models._v1_comments_get_200_response_data_inner._v1_comments_get_200_response_data_inner(
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
                        dislikes = 1.337, )
                    ]
            )
        else:
            return V1CommentsGet200Response(
                success = true,
                data = [
                    shionstream_sdk.models._v1_comments_get_200_response_data_inner._v1_comments_get_200_response_data_inner(
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
                        dislikes = 1.337, )
                    ],
        )
        """

    def testV1CommentsGet200Response(self):
        """Test V1CommentsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
