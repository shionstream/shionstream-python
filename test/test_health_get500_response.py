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

from shionstream_sdk.models.health_get500_response import HealthGet500Response

class TestHealthGet500Response(unittest.TestCase):
    """HealthGet500Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HealthGet500Response:
        """Test HealthGet500Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HealthGet500Response`
        """
        model = HealthGet500Response()
        if include_optional:
            return HealthGet500Response(
                status = 'ok',
                timestamp = '',
                database = '',
                error = ''
            )
        else:
            return HealthGet500Response(
                status = 'ok',
                timestamp = '',
                database = '',
        )
        """

    def testHealthGet500Response(self):
        """Test HealthGet500Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
