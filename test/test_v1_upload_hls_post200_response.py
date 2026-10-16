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

from shionstream_sdk.models.v1_upload_hls_post200_response import V1UploadHlsPost200Response

class TestV1UploadHlsPost200Response(unittest.TestCase):
    """V1UploadHlsPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1UploadHlsPost200Response:
        """Test V1UploadHlsPost200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1UploadHlsPost200Response`
        """
        model = V1UploadHlsPost200Response()
        if include_optional:
            return V1UploadHlsPost200Response(
                success = true,
                data = shionstream_sdk.models._v1_upload_hls_post_200_response_data._v1_upload_hls_post_200_response_data(
                    url = '', 
                    key = '', 
                    size_bytes = 1.337, 
                    total_files = 1.337, )
            )
        else:
            return V1UploadHlsPost200Response(
                success = true,
                data = shionstream_sdk.models._v1_upload_hls_post_200_response_data._v1_upload_hls_post_200_response_data(
                    url = '', 
                    key = '', 
                    size_bytes = 1.337, 
                    total_files = 1.337, ),
        )
        """

    def testV1UploadHlsPost200Response(self):
        """Test V1UploadHlsPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
