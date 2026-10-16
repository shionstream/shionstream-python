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

from shionstream_sdk.models.v1_dashboard_categories_get200_response_categories_inner import V1DashboardCategoriesGet200ResponseCategoriesInner

class TestV1DashboardCategoriesGet200ResponseCategoriesInner(unittest.TestCase):
    """V1DashboardCategoriesGet200ResponseCategoriesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DashboardCategoriesGet200ResponseCategoriesInner:
        """Test V1DashboardCategoriesGet200ResponseCategoriesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DashboardCategoriesGet200ResponseCategoriesInner`
        """
        model = V1DashboardCategoriesGet200ResponseCategoriesInner()
        if include_optional:
            return V1DashboardCategoriesGet200ResponseCategoriesInner(
                id = '',
                code = '',
                name = '',
                slug = '',
                anime_count = 1.337,
                description = '',
                is_active = True,
                updated_at = ''
            )
        else:
            return V1DashboardCategoriesGet200ResponseCategoriesInner(
                id = '',
                code = '',
                name = '',
                slug = '',
                anime_count = 1.337,
                description = '',
                is_active = True,
                updated_at = '',
        )
        """

    def testV1DashboardCategoriesGet200ResponseCategoriesInner(self):
        """Test V1DashboardCategoriesGet200ResponseCategoriesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
