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

from shionstream_sdk.api.comments_api import CommentsApi


class TestCommentsApi(unittest.TestCase):
    """CommentsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CommentsApi()

    def tearDown(self) -> None:
        pass

    def test_v1_comments_get(self) -> None:
        """Test case for v1_comments_get

        Get Episode Comments
        """
        pass

    def test_v1_comments_id_like_post(self) -> None:
        """Test case for v1_comments_id_like_post

        Like or Dislike Comment
        """
        pass

    def test_v1_comments_id_report_post(self) -> None:
        """Test case for v1_comments_id_report_post

        Report Comment
        """
        pass

    def test_v1_comments_post(self) -> None:
        """Test case for v1_comments_post

        Create Comment
        """
        pass


if __name__ == '__main__':
    unittest.main()
