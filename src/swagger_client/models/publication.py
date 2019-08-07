# coding: utf-8

"""
    mzTab validation API.

    This is an mzTab validation service.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: nils.hoffmann@isas.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.indexed_element import IndexedElement  # noqa: F401,E501
from swagger_client.models.publication_item import PublicationItem  # noqa: F401,E501


class Publication(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'publication_items': 'list[PublicationItem]'
    }

    attribute_map = {
        'publication_items': 'publicationItems'
    }

    def __init__(self, publication_items=None):  # noqa: E501
        """Publication - a model defined in Swagger"""  # noqa: E501

        self._publication_items = None
        self.discriminator = None

        self.publication_items = publication_items

    @property
    def publication_items(self):
        """Gets the publication_items of this Publication.  # noqa: E501


        :return: The publication_items of this Publication.  # noqa: E501
        :rtype: list[PublicationItem]
        """
        return self._publication_items

    @publication_items.setter
    def publication_items(self, publication_items):
        """Sets the publication_items of this Publication.


        :param publication_items: The publication_items of this Publication.  # noqa: E501
        :type: list[PublicationItem]
        """
        if publication_items is None:
            raise ValueError("Invalid value for `publication_items`, must not be `None`")  # noqa: E501

        self._publication_items = publication_items

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Publication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
    def to_lines(self):
        # 'publication_items': 'list[PublicationItem]'
        l = [e.as_line() for e in self.publication_items] # could use lambda, this is more readable
        text = '|'.join(l)
        return ['\t{}'.format(text)]

    @staticmethod
    def fromText(text):
        publication_items = []
        for pi in text.split('|'):
            publication_items.append(PublicationItem.fromText(pi.strip()))
        
        return Publication(publication_items)