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

from shionstream_sdk.models.v1_user_settings_patch_request_player import V1UserSettingsPatchRequestPlayer

class TestV1UserSettingsPatchRequestPlayer(unittest.TestCase):
    """V1UserSettingsPatchRequestPlayer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1UserSettingsPatchRequestPlayer:
        """Test V1UserSettingsPatchRequestPlayer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1UserSettingsPatchRequestPlayer`
        """
        model = V1UserSettingsPatchRequestPlayer()
        if include_optional:
            return V1UserSettingsPatchRequestPlayer(
                default_quality = '',
                default_subtitle = '',
                auto_play_next = True,
                auto_skip_intro = True,
                preferred_audio = ''
            )
        else:
            return V1UserSettingsPatchRequestPlayer(
        )
        """

    def testV1UserSettingsPatchRequestPlayer(self):
        """Test V1UserSettingsPatchRequestPlayer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
