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

from shionstream_sdk.api.sample_api import SampleApi


class TestSampleApi(unittest.TestCase):
    """SampleApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SampleApi()

    def tearDown(self) -> None:
        pass

    def test_v1_protected_sample_get(self) -> None:
        """Test case for v1_protected_sample_get

        Protected Sample Endpoint
        """
        pass


if __name__ == '__main__':
    unittest.main()
