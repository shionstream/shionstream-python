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

from shionstream_sdk.models.v1_episodes_id_stream_get200_response_subtitles_inner import V1EpisodesIdStreamGet200ResponseSubtitlesInner

class TestV1EpisodesIdStreamGet200ResponseSubtitlesInner(unittest.TestCase):
    """V1EpisodesIdStreamGet200ResponseSubtitlesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1EpisodesIdStreamGet200ResponseSubtitlesInner:
        """Test V1EpisodesIdStreamGet200ResponseSubtitlesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1EpisodesIdStreamGet200ResponseSubtitlesInner`
        """
        model = V1EpisodesIdStreamGet200ResponseSubtitlesInner()
        if include_optional:
            return V1EpisodesIdStreamGet200ResponseSubtitlesInner(
                id = '',
                label = '',
                language_code = '',
                file_url = '',
                format = '',
                is_default = True
            )
        else:
            return V1EpisodesIdStreamGet200ResponseSubtitlesInner(
                id = '',
                label = '',
                language_code = '',
                file_url = '',
                format = '',
                is_default = True,
        )
        """

    def testV1EpisodesIdStreamGet200ResponseSubtitlesInner(self):
        """Test V1EpisodesIdStreamGet200ResponseSubtitlesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
