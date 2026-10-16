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

from shionstream_sdk.models.v1_episodes_id_stream_get200_response import V1EpisodesIdStreamGet200Response

class TestV1EpisodesIdStreamGet200Response(unittest.TestCase):
    """V1EpisodesIdStreamGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1EpisodesIdStreamGet200Response:
        """Test V1EpisodesIdStreamGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1EpisodesIdStreamGet200Response`
        """
        model = V1EpisodesIdStreamGet200Response()
        if include_optional:
            return V1EpisodesIdStreamGet200Response(
                success = true,
                episode = shionstream_sdk.models._v1_episodes__id__stream_get_200_response_episode._v1_episodes__id__stream_get_200_response_episode(
                    id = '', 
                    anime_id = '', 
                    number = 1.337, 
                    title = '', ),
                sources = [
                    shionstream_sdk.models._v1_episodes__id__stream_get_200_response_sources_inner._v1_episodes__id__stream_get_200_response_sources_inner(
                        id = '', 
                        server_name = '', 
                        stream_url = '', 
                        format = '', 
                        quality = '', 
                        url1080p = '', 
                        url720p = '', 
                        url480p = '', 
                        url360p = '', 
                        is_primary = True, )
                    ],
                subtitles = [
                    shionstream_sdk.models._v1_episodes__id__stream_get_200_response_subtitles_inner._v1_episodes__id__stream_get_200_response_subtitles_inner(
                        id = '', 
                        label = '', 
                        language_code = '', 
                        file_url = '', 
                        format = '', 
                        is_default = True, )
                    ],
                audio = [
                    shionstream_sdk.models._v1_episodes__id__stream_get_200_response_audio_inner._v1_episodes__id__stream_get_200_response_audio_inner(
                        id = '', 
                        label = '', 
                        language_code = '', 
                        audio_url = '', 
                        type = '', 
                        is_default = True, )
                    ]
            )
        else:
            return V1EpisodesIdStreamGet200Response(
                success = true,
                episode = shionstream_sdk.models._v1_episodes__id__stream_get_200_response_episode._v1_episodes__id__stream_get_200_response_episode(
                    id = '', 
                    anime_id = '', 
                    number = 1.337, 
                    title = '', ),
                sources = [
                    shionstream_sdk.models._v1_episodes__id__stream_get_200_response_sources_inner._v1_episodes__id__stream_get_200_response_sources_inner(
                        id = '', 
                        server_name = '', 
                        stream_url = '', 
                        format = '', 
                        quality = '', 
                        url1080p = '', 
                        url720p = '', 
                        url480p = '', 
                        url360p = '', 
                        is_primary = True, )
                    ],
                subtitles = [
                    shionstream_sdk.models._v1_episodes__id__stream_get_200_response_subtitles_inner._v1_episodes__id__stream_get_200_response_subtitles_inner(
                        id = '', 
                        label = '', 
                        language_code = '', 
                        file_url = '', 
                        format = '', 
                        is_default = True, )
                    ],
                audio = [
                    shionstream_sdk.models._v1_episodes__id__stream_get_200_response_audio_inner._v1_episodes__id__stream_get_200_response_audio_inner(
                        id = '', 
                        label = '', 
                        language_code = '', 
                        audio_url = '', 
                        type = '', 
                        is_default = True, )
                    ],
        )
        """

    def testV1EpisodesIdStreamGet200Response(self):
        """Test V1EpisodesIdStreamGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
