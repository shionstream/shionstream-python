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

from shionstream_sdk.models.v1_episodes_id_stream_get200_response_sources_inner import V1EpisodesIdStreamGet200ResponseSourcesInner

class TestV1EpisodesIdStreamGet200ResponseSourcesInner(unittest.TestCase):
    """V1EpisodesIdStreamGet200ResponseSourcesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1EpisodesIdStreamGet200ResponseSourcesInner:
        """Test V1EpisodesIdStreamGet200ResponseSourcesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1EpisodesIdStreamGet200ResponseSourcesInner`
        """
        model = V1EpisodesIdStreamGet200ResponseSourcesInner()
        if include_optional:
            return V1EpisodesIdStreamGet200ResponseSourcesInner(
                id = '',
                server_name = '',
                stream_url = '',
                format = '',
                quality = '',
                url1080p = '',
                url720p = '',
                url480p = '',
                url360p = '',
                is_primary = True
            )
        else:
            return V1EpisodesIdStreamGet200ResponseSourcesInner(
                id = '',
                stream_url = '',
                format = '',
                quality = '',
                is_primary = True,
        )
        """

    def testV1EpisodesIdStreamGet200ResponseSourcesInner(self):
        """Test V1EpisodesIdStreamGet200ResponseSourcesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
