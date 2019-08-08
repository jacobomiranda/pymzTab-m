# coding: utf-8

"""
    mzTab-M reference implementation and validation API.

    This is the mzTab-M reference implementation and validation API service.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: nils.hoffmann@isas.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

import unittest

import swagger_client
from swagger_client.models.metadata import Metadata  # noqa: E501
from swagger_client.rest import ApiException


class TestMetadata(unittest.TestCase):
    """Metadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetadata(self):
        """Test Metadata"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.metadata.Metadata()  # noqa: E501
        pass

    def testMzTabVersion(self):
        """Test mzTab version"""
        mzTabVersion = "2.0.0-M"
        self.assertTrue(re.fullmatch(r'^\d{1}\.\d{1}\.\d{1}-[A-Z]{1}$', mzTabVersion))


if __name__ == '__main__':
    unittest.main()
