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

from shionstream_sdk.models.v1_dashboard_moderation_get200_response_reports_inner import V1DashboardModerationGet200ResponseReportsInner

class TestV1DashboardModerationGet200ResponseReportsInner(unittest.TestCase):
    """V1DashboardModerationGet200ResponseReportsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DashboardModerationGet200ResponseReportsInner:
        """Test V1DashboardModerationGet200ResponseReportsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DashboardModerationGet200ResponseReportsInner`
        """
        model = V1DashboardModerationGet200ResponseReportsInner()
        if include_optional:
            return V1DashboardModerationGet200ResponseReportsInner(
                id = '',
                comment_id = '',
                comment_text = '',
                anime_title = '',
                episode_number = 1.337,
                author = shionstream_sdk.models._v1_dashboard_moderation_get_200_response_reports_inner_author._v1_dashboard_moderation_get_200_response_reports_inner_author(
                    id = '', 
                    name = '', 
                    username = '', 
                    avatar = '', ),
                reporter = shionstream_sdk.models._v1_dashboard_moderation_get_200_response_reports_inner_reporter._v1_dashboard_moderation_get_200_response_reports_inner_reporter(
                    id = '', 
                    name = '', 
                    username = '', ),
                reason = '',
                status = '',
                reported_at = '',
                flagged_by_system = True
            )
        else:
            return V1DashboardModerationGet200ResponseReportsInner(
                id = '',
                comment_id = '',
                comment_text = '',
                anime_title = '',
                episode_number = 1.337,
                author = shionstream_sdk.models._v1_dashboard_moderation_get_200_response_reports_inner_author._v1_dashboard_moderation_get_200_response_reports_inner_author(
                    id = '', 
                    name = '', 
                    username = '', 
                    avatar = '', ),
                reporter = shionstream_sdk.models._v1_dashboard_moderation_get_200_response_reports_inner_reporter._v1_dashboard_moderation_get_200_response_reports_inner_reporter(
                    id = '', 
                    name = '', 
                    username = '', ),
                reason = '',
                status = '',
                reported_at = '',
                flagged_by_system = True,
        )
        """

    def testV1DashboardModerationGet200ResponseReportsInner(self):
        """Test V1DashboardModerationGet200ResponseReportsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
