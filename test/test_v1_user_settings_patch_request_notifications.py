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

from shionstream_sdk.models.v1_user_settings_patch_request_notifications import V1UserSettingsPatchRequestNotifications

class TestV1UserSettingsPatchRequestNotifications(unittest.TestCase):
    """V1UserSettingsPatchRequestNotifications unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1UserSettingsPatchRequestNotifications:
        """Test V1UserSettingsPatchRequestNotifications
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1UserSettingsPatchRequestNotifications`
        """
        model = V1UserSettingsPatchRequestNotifications()
        if include_optional:
            return V1UserSettingsPatchRequestNotifications(
                new_episode_alerts = True,
                watchlist_updates = True,
                marketing_emails = True,
                public_watchlist = True
            )
        else:
            return V1UserSettingsPatchRequestNotifications(
        )
        """

    def testV1UserSettingsPatchRequestNotifications(self):
        """Test V1UserSettingsPatchRequestNotifications"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
