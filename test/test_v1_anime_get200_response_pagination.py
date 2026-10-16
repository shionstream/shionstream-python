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

from shionstream_sdk.models.v1_anime_get200_response_pagination import V1AnimeGet200ResponsePagination

class TestV1AnimeGet200ResponsePagination(unittest.TestCase):
    """V1AnimeGet200ResponsePagination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1AnimeGet200ResponsePagination:
        """Test V1AnimeGet200ResponsePagination
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1AnimeGet200ResponsePagination`
        """
        model = V1AnimeGet200ResponsePagination()
        if include_optional:
            return V1AnimeGet200ResponsePagination(
                page = 1.337,
                limit = 1.337,
                total = 1.337,
                total_pages = 1.337
            )
        else:
            return V1AnimeGet200ResponsePagination(
                page = 1.337,
                limit = 1.337,
                total = 1.337,
                total_pages = 1.337,
        )
        """

    def testV1AnimeGet200ResponsePagination(self):
        """Test V1AnimeGet200ResponsePagination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
