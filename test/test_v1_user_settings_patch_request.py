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

from shionstream_sdk.models.v1_user_settings_patch_request import V1UserSettingsPatchRequest

class TestV1UserSettingsPatchRequest(unittest.TestCase):
    """V1UserSettingsPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1UserSettingsPatchRequest:
        """Test V1UserSettingsPatchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1UserSettingsPatchRequest`
        """
        model = V1UserSettingsPatchRequest()
        if include_optional:
            return V1UserSettingsPatchRequest(
                profile = shionstream_sdk.models._v1_user_settings_patch_request_profile._v1_user_settings_patch_request_profile(
                    display_name = '', 
                    bio = '', 
                    avatar_url = '', ),
                player = shionstream_sdk.models._v1_user_settings_patch_request_player._v1_user_settings_patch_request_player(
                    default_quality = '', 
                    default_subtitle = '', 
                    auto_play_next = True, 
                    auto_skip_intro = True, 
                    preferred_audio = '', ),
                notifications = shionstream_sdk.models._v1_user_settings_patch_request_notifications._v1_user_settings_patch_request_notifications(
                    new_episode_alerts = True, 
                    watchlist_updates = True, 
                    marketing_emails = True, 
                    public_watchlist = True, )
            )
        else:
            return V1UserSettingsPatchRequest(
        )
        """

    def testV1UserSettingsPatchRequest(self):
        """Test V1UserSettingsPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
