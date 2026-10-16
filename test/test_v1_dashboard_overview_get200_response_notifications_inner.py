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

from shionstream_sdk.models.v1_dashboard_overview_get200_response_notifications_inner import V1DashboardOverviewGet200ResponseNotificationsInner

class TestV1DashboardOverviewGet200ResponseNotificationsInner(unittest.TestCase):
    """V1DashboardOverviewGet200ResponseNotificationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DashboardOverviewGet200ResponseNotificationsInner:
        """Test V1DashboardOverviewGet200ResponseNotificationsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DashboardOverviewGet200ResponseNotificationsInner`
        """
        model = V1DashboardOverviewGet200ResponseNotificationsInner()
        if include_optional:
            return V1DashboardOverviewGet200ResponseNotificationsInner(
                id = '',
                title = '',
                description = '',
                time = '',
                type = 'success'
            )
        else:
            return V1DashboardOverviewGet200ResponseNotificationsInner(
                id = '',
                title = '',
                description = '',
                time = '',
                type = 'success',
        )
        """

    def testV1DashboardOverviewGet200ResponseNotificationsInner(self):
        """Test V1DashboardOverviewGet200ResponseNotificationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
