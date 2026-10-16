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


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "shionstream-sdk"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">= 3.10"
REQUIRES = [
    "urllib3 >= 2.7.0, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2.11",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="ShionStream API",
    author="ShionStream Engineering Team",
    author_email="dev@gox.my.id",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "ShionStream API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache-2.0",
    long_description_content_type='text/markdown',
    long_description="""\
    Modular anime streaming and metadata API built with Hono on Cloudflare Workers.
    """,  # noqa: E501
    package_data={"shionstream_sdk": ["py.typed"]},
)
