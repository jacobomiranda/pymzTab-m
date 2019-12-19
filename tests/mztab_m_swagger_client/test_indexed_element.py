# coding: utf-8

"""
    mzTab-M reference implementation and validation API.

    This is the mzTab-M reference implementation and validation API service.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: nils.hoffmann@isas.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import mztab_m_swagger_client
from mztab_m_swagger_client.models.indexed_element import IndexedElement  # noqa: E501
from mztab_m_swagger_client.rest import ApiException


class TestIndexedElement(unittest.TestCase):
    """IndexedElement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIndexedElement(self):
        """Test IndexedElement"""
        model = mztab_m_swagger_client.models.indexed_element.IndexedElement(id=1)
        print(model)
        print(model.to_dict())
        self.assertEqual(1, model.id)
        self.assertEqual('element_type', model.element_type)
        pass


if __name__ == '__main__':
    unittest.main()