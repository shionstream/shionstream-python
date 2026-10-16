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

from shionstream_sdk.models.v1_dashboard_roles_get200_response import V1DashboardRolesGet200Response

class TestV1DashboardRolesGet200Response(unittest.TestCase):
    """V1DashboardRolesGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1DashboardRolesGet200Response:
        """Test V1DashboardRolesGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1DashboardRolesGet200Response`
        """
        model = V1DashboardRolesGet200Response()
        if include_optional:
            return V1DashboardRolesGet200Response(
                roles = [
                    shionstream_sdk.models._v1_dashboard_roles_get_200_response_roles_inner._v1_dashboard_roles_get_200_response_roles_inner(
                        id = '', 
                        name = '', 
                        slug = '', 
                        description = '', 
                        member_count = 1.337, 
                        permissions = [
                            ''
                            ], 
                        is_default = True, )
                    ]
            )
        else:
            return V1DashboardRolesGet200Response(
                roles = [
                    shionstream_sdk.models._v1_dashboard_roles_get_200_response_roles_inner._v1_dashboard_roles_get_200_response_roles_inner(
                        id = '', 
                        name = '', 
                        slug = '', 
                        description = '', 
                        member_count = 1.337, 
                        permissions = [
                            ''
                            ], 
                        is_default = True, )
                    ],
        )
        """

    def testV1DashboardRolesGet200Response(self):
        """Test V1DashboardRolesGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
