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

from shionstream_sdk.models.v1_dashboard_seasons_get200_response_seasons_inner import V1DashboardSeasonsGet200ResponseSeasonsInner

class TestV1DashboardSeasonsGet200ResponseSeasonsInner(unittest.TestCase):
    """V1DashboardSeasonsGet200ResponseSeasonsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DashboardSeasonsGet200ResponseSeasonsInner:
        """Test V1DashboardSeasonsGet200ResponseSeasonsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DashboardSeasonsGet200ResponseSeasonsInner`
        """
        model = V1DashboardSeasonsGet200ResponseSeasonsInner()
        if include_optional:
            return V1DashboardSeasonsGet200ResponseSeasonsInner(
                id = '',
                year = 1.337,
                quarter = '',
                name = '',
                total_anime = 1.337,
                is_current = True,
                is_active = True
            )
        else:
            return V1DashboardSeasonsGet200ResponseSeasonsInner(
                id = '',
                year = 1.337,
                quarter = '',
                name = '',
                total_anime = 1.337,
                is_current = True,
                is_active = True,
        )
        """

    def testV1DashboardSeasonsGet200ResponseSeasonsInner(self):
        """Test V1DashboardSeasonsGet200ResponseSeasonsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
