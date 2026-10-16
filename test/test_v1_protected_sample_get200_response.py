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

from shionstream_sdk.models.v1_protected_sample_get200_response import V1ProtectedSampleGet200Response

class TestV1ProtectedSampleGet200Response(unittest.TestCase):
    """V1ProtectedSampleGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ProtectedSampleGet200Response:
        """Test V1ProtectedSampleGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ProtectedSampleGet200Response`
        """
        model = V1ProtectedSampleGet200Response()
        if include_optional:
            return V1ProtectedSampleGet200Response(
                success = true,
                message = '',
                user = shionstream_sdk.models._v1_protected_sample_get_200_response_user._v1_protected_sample_get_200_response_user(
                    id = '', 
                    name = '', 
                    email = '', 
                    role = '', )
            )
        else:
            return V1ProtectedSampleGet200Response(
                success = true,
                message = '',
                user = shionstream_sdk.models._v1_protected_sample_get_200_response_user._v1_protected_sample_get_200_response_user(
                    id = '', 
                    name = '', 
                    email = '', 
                    role = '', ),
        )
        """

    def testV1ProtectedSampleGet200Response(self):
        """Test V1ProtectedSampleGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
