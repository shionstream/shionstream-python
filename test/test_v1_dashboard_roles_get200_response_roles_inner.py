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

from shionstream_sdk.models.v1_dashboard_roles_get200_response_roles_inner import V1DashboardRolesGet200ResponseRolesInner

class TestV1DashboardRolesGet200ResponseRolesInner(unittest.TestCase):
    """V1DashboardRolesGet200ResponseRolesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DashboardRolesGet200ResponseRolesInner:
        """Test V1DashboardRolesGet200ResponseRolesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DashboardRolesGet200ResponseRolesInner`
        """
        model = V1DashboardRolesGet200ResponseRolesInner()
        if include_optional:
            return V1DashboardRolesGet200ResponseRolesInner(
                id = '',
                name = '',
                slug = '',
                description = '',
                member_count = 1.337,
                permissions = [
                    ''
                    ],
                is_default = True
            )
        else:
            return V1DashboardRolesGet200ResponseRolesInner(
                id = '',
                name = '',
                slug = '',
                description = '',
                member_count = 1.337,
                permissions = [
                    ''
                    ],
        )
        """

    def testV1DashboardRolesGet200ResponseRolesInner(self):
        """Test V1DashboardRolesGet200ResponseRolesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
