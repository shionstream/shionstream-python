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

from shionstream_sdk.models.health_get200_response import HealthGet200Response

class TestHealthGet200Response(unittest.TestCase):
    """HealthGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HealthGet200Response:
        """Test HealthGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HealthGet200Response`
        """
        model = HealthGet200Response()
        if include_optional:
            return HealthGet200Response(
                status = 'ok',
                timestamp = '',
                database = ''
            )
        else:
            return HealthGet200Response(
                status = 'ok',
                timestamp = '',
                database = '',
        )
        """

    def testHealthGet200Response(self):
        """Test HealthGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
