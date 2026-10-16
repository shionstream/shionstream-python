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

from shionstream_sdk.models.v1_upload_hls_post200_response_data import V1UploadHlsPost200ResponseData

class TestV1UploadHlsPost200ResponseData(unittest.TestCase):
    """V1UploadHlsPost200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1UploadHlsPost200ResponseData:
        """Test V1UploadHlsPost200ResponseData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1UploadHlsPost200ResponseData`
        """
        model = V1UploadHlsPost200ResponseData()
        if include_optional:
            return V1UploadHlsPost200ResponseData(
                url = '',
                key = '',
                size_bytes = 1.337,
                total_files = 1.337
            )
        else:
            return V1UploadHlsPost200ResponseData(
                url = '',
                key = '',
                size_bytes = 1.337,
                total_files = 1.337,
        )
        """

    def testV1UploadHlsPost200ResponseData(self):
        """Test V1UploadHlsPost200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
