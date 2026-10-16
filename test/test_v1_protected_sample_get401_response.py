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

from shionstream_sdk.models.v1_protected_sample_get401_response import V1ProtectedSampleGet401Response

class TestV1ProtectedSampleGet401Response(unittest.TestCase):
    """V1ProtectedSampleGet401Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ProtectedSampleGet401Response:
        """Test V1ProtectedSampleGet401Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ProtectedSampleGet401Response`
        """
        model = V1ProtectedSampleGet401Response()
        if include_optional:
            return V1ProtectedSampleGet401Response(
                success = false,
                error = ''
            )
        else:
            return V1ProtectedSampleGet401Response(
                success = false,
                error = '',
        )
        """

    def testV1ProtectedSampleGet401Response(self):
        """Test V1ProtectedSampleGet401Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
