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

from swagger_client.models.parameter import Parameter  # noqa: F401,E501


class ColumnParameterMapping(object):
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
        'column_name': 'str',
        'param': 'Parameter'
    }

    attribute_map = {
        'column_name': 'column_name',
        'param': 'param'
    }

    def __init__(self, column_name=None, param=None):  # noqa: E501
        """ColumnParameterMapping - a model defined in Swagger"""  # noqa: E501

        self._column_name = None
        self._param = None
        self.discriminator = None

        self.column_name = column_name
        self.param = param

    @property
    def column_name(self):
        """Gets the column_name of this ColumnParameterMapping.  # noqa: E501


        :return: The column_name of this ColumnParameterMapping.  # noqa: E501
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this ColumnParameterMapping.


        :param column_name: The column_name of this ColumnParameterMapping.  # noqa: E501
        :type: str
        """
        if column_name is None:
            raise ValueError("Invalid value for `column_name`, must not be `None`")  # noqa: E501

        self._column_name = column_name

    @property
    def param(self):
        """Gets the param of this ColumnParameterMapping.  # noqa: E501


        :return: The param of this ColumnParameterMapping.  # noqa: E501
        :rtype: Parameter
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this ColumnParameterMapping.


        :param param: The param of this ColumnParameterMapping.  # noqa: E501
        :type: Parameter
        """
        if param is None:
            raise ValueError("Invalid value for `param`, must not be `None`")  # noqa: E501

        self._param = param

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
        if not isinstance(other, ColumnParameterMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
    
    def as_line(self):
        return '{}={}'.format(self.column_name, self.param.as_line())
    
