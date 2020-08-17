# coding: utf-8

"""
    mzTab-M reference implementation and validation API.

    This is the mzTab-M reference implementation and validation API service.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: nils.hoffmann@isas.de
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ValidationMessage(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'code': 'str',
        'category': 'str',
        'message_type': 'str',
        'message': 'str',
        'line_number': 'int'
    }

    attribute_map = {
        'code': 'code',
        'category': 'category',
        'message_type': 'message_type',
        'message': 'message',
        'line_number': 'line_number'
    }

    def __init__(self, code=None, category='format', message_type='info', message=None, line_number=None, local_vars_configuration=None):  # noqa: E501
        """ValidationMessage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._category = None
        self._message_type = None
        self._message = None
        self._line_number = None
        self.discriminator = None

        self.code = code
        self.category = category
        if message_type is not None:
            self.message_type = message_type
        self.message = message
        if line_number is not None:
            self.line_number = line_number

    @property
    def code(self):
        """Gets the code of this ValidationMessage.  # noqa: E501


        :return: The code of this ValidationMessage.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ValidationMessage.


        :param code: The code of this ValidationMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def category(self):
        """Gets the category of this ValidationMessage.  # noqa: E501


        :return: The category of this ValidationMessage.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ValidationMessage.


        :param category: The category of this ValidationMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and category is None:  # noqa: E501
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501
        allowed_values = ["format", "logical", "cross_check"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and category not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def message_type(self):
        """Gets the message_type of this ValidationMessage.  # noqa: E501


        :return: The message_type of this ValidationMessage.  # noqa: E501
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this ValidationMessage.


        :param message_type: The message_type of this ValidationMessage.  # noqa: E501
        :type: str
        """
        allowed_values = ["error", "warn", "info"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and message_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `message_type` ({0}), must be one of {1}"  # noqa: E501
                .format(message_type, allowed_values)
            )

        self._message_type = message_type

    @property
    def message(self):
        """Gets the message of this ValidationMessage.  # noqa: E501


        :return: The message of this ValidationMessage.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ValidationMessage.


        :param message: The message of this ValidationMessage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def line_number(self):
        """Gets the line_number of this ValidationMessage.  # noqa: E501


        :return: The line_number of this ValidationMessage.  # noqa: E501
        :rtype: int
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        """Sets the line_number of this ValidationMessage.


        :param line_number: The line_number of this ValidationMessage.  # noqa: E501
        :type: int
        """

        self._line_number = line_number

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, ValidationMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValidationMessage):
            return True

        return self.to_dict() != other.to_dict()
