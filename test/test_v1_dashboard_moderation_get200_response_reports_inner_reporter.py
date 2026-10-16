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

from shionstream_sdk.models.v1_dashboard_moderation_get200_response_reports_inner_reporter import V1DashboardModerationGet200ResponseReportsInnerReporter

class TestV1DashboardModerationGet200ResponseReportsInnerReporter(unittest.TestCase):
    """V1DashboardModerationGet200ResponseReportsInnerReporter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DashboardModerationGet200ResponseReportsInnerReporter:
        """Test V1DashboardModerationGet200ResponseReportsInnerReporter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DashboardModerationGet200ResponseReportsInnerReporter`
        """
        model = V1DashboardModerationGet200ResponseReportsInnerReporter()
        if include_optional:
            return V1DashboardModerationGet200ResponseReportsInnerReporter(
                id = '',
                name = '',
                username = ''
            )
        else:
            return V1DashboardModerationGet200ResponseReportsInnerReporter(
                id = '',
                name = '',
                username = '',
        )
        """

    def testV1DashboardModerationGet200ResponseReportsInnerReporter(self):
        """Test V1DashboardModerationGet200ResponseReportsInnerReporter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
