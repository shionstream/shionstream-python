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

from shionstream_sdk.models.v1_dashboard_users_get200_response_users_inner import V1DashboardUsersGet200ResponseUsersInner

class TestV1DashboardUsersGet200ResponseUsersInner(unittest.TestCase):
    """V1DashboardUsersGet200ResponseUsersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DashboardUsersGet200ResponseUsersInner:
        """Test V1DashboardUsersGet200ResponseUsersInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DashboardUsersGet200ResponseUsersInner`
        """
        model = V1DashboardUsersGet200ResponseUsersInner()
        if include_optional:
            return V1DashboardUsersGet200ResponseUsersInner(
                id = '',
                name = '',
                email = '',
                image = '',
                role = '',
                email_verified = True,
                created_at = ''
            )
        else:
            return V1DashboardUsersGet200ResponseUsersInner(
                id = '',
                name = '',
                email = '',
                role = '',
                email_verified = True,
                created_at = '',
        )
        """

    def testV1DashboardUsersGet200ResponseUsersInner(self):
        """Test V1DashboardUsersGet200ResponseUsersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
