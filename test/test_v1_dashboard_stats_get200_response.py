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

from shionstream_sdk.models.v1_dashboard_stats_get200_response import V1DashboardStatsGet200Response

class TestV1DashboardStatsGet200Response(unittest.TestCase):
    """V1DashboardStatsGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DashboardStatsGet200Response:
        """Test V1DashboardStatsGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DashboardStatsGet200Response`
        """
        model = V1DashboardStatsGet200Response()
        if include_optional:
            return V1DashboardStatsGet200Response(
                stats = shionstream_sdk.models._v1_dashboard_stats_get_200_response_stats._v1_dashboard_stats_get_200_response_stats(
                    total_anime = 1.337, 
                    total_episodes = 1.337, 
                    total_users = 1.337, 
                    pending_reports = 1.337, 
                    active_streams = 1.337, 
                    bandwidth_usage_gb = 1.337, 
                    cpu_load_percent = 1.337, 
                    storage_used_gb = 1.337, 
                    monthly_growth_percent = 1.337, )
            )
        else:
            return V1DashboardStatsGet200Response(
                stats = shionstream_sdk.models._v1_dashboard_stats_get_200_response_stats._v1_dashboard_stats_get_200_response_stats(
                    total_anime = 1.337, 
                    total_episodes = 1.337, 
                    total_users = 1.337, 
                    pending_reports = 1.337, 
                    active_streams = 1.337, 
                    bandwidth_usage_gb = 1.337, 
                    cpu_load_percent = 1.337, 
                    storage_used_gb = 1.337, 
                    monthly_growth_percent = 1.337, ),
        )
        """

    def testV1DashboardStatsGet200Response(self):
        """Test V1DashboardStatsGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
