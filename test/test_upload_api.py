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

from shionstream_sdk.api.upload_api import UploadApi


class TestUploadApi(unittest.TestCase):
    """UploadApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UploadApi()

    def tearDown(self) -> None:
        pass

    def test_v1_upload_hls_post(self) -> None:
        """Test case for v1_upload_hls_post

        Upload HLS Package to Cloudflare R2
        """
        pass

    def test_v1_upload_image_post(self) -> None:
        """Test case for v1_upload_image_post

        Upload Image to Cloudflare R2
        """
        pass


if __name__ == '__main__':
    unittest.main()
