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

from shionstream_sdk.models.v1_dashboard_categories_get200_response_genres_inner import V1DashboardCategoriesGet200ResponseGenresInner

class TestV1DashboardCategoriesGet200ResponseGenresInner(unittest.TestCase):
    """V1DashboardCategoriesGet200ResponseGenresInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DashboardCategoriesGet200ResponseGenresInner:
        """Test V1DashboardCategoriesGet200ResponseGenresInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DashboardCategoriesGet200ResponseGenresInner`
        """
        model = V1DashboardCategoriesGet200ResponseGenresInner()
        if include_optional:
            return V1DashboardCategoriesGet200ResponseGenresInner(
                id = '',
                name = '',
                slug = '',
                anime_count = 1.337,
                is_active = True
            )
        else:
            return V1DashboardCategoriesGet200ResponseGenresInner(
                id = '',
                name = '',
                slug = '',
                anime_count = 1.337,
                is_active = True,
        )
        """

    def testV1DashboardCategoriesGet200ResponseGenresInner(self):
        """Test V1DashboardCategoriesGet200ResponseGenresInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
