# coding: utf-8

"""
    mzTab-M reference implementation and validation API.

    This is the mzTab-M reference implementation and validation API service.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: nils.hoffmann@isas.de
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.validate_api import ValidateApi  # noqa: E501
from openapi_client.rest import ApiException


class TestValidateApi(unittest.TestCase):
    """ValidateApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.validate_api.ValidateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_validate_mz_tab_file(self):
        """Test case for validate_mz_tab_file

        """
        pass


if __name__ == '__main__':
    unittest.main()
