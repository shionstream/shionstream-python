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

from shionstream_sdk.models.v1_user_settings_patch_request_profile import V1UserSettingsPatchRequestProfile

class TestV1UserSettingsPatchRequestProfile(unittest.TestCase):
    """V1UserSettingsPatchRequestProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1UserSettingsPatchRequestProfile:
        """Test V1UserSettingsPatchRequestProfile
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1UserSettingsPatchRequestProfile`
        """
        model = V1UserSettingsPatchRequestProfile()
        if include_optional:
            return V1UserSettingsPatchRequestProfile(
                display_name = '',
                bio = '',
                avatar_url = ''
            )
        else:
            return V1UserSettingsPatchRequestProfile(
        )
        """

    def testV1UserSettingsPatchRequestProfile(self):
        """Test V1UserSettingsPatchRequestProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
