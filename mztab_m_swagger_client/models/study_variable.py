# coding: utf-8

"""
    mzTab-M reference implementation and validation API.

    This is the mzTab-M reference implementation and validation API service.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: nils.hoffmann@isas.de
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mztab_m_swagger_client.models.assay import Assay  # noqa: F401,E501
from mztab_m_swagger_client.models.indexed_element import IndexedElement  # noqa: F401,E501
from mztab_m_swagger_client.models.parameter import Parameter  # noqa: F401,E501


class StudyVariable(IndexedElement):
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
        'name': 'str',
        'assay_refs': 'list[Assay]',
        'average_function': 'Parameter',
        'variation_function': 'Parameter',
        'description': 'str',
        'factors': 'list[Parameter]'
    }

    attribute_map = {
        'name': 'name',
        'assay_refs': 'assay_refs',
        'average_function': 'average_function',
        'variation_function': 'variation_function',
        'description': 'description',
        'factors': 'factors'
    }

    def __init__(self, name=None, assay_refs=None, average_function=None, variation_function=None, description=None, factors=None, **kwargs):  # noqa: E501
        """StudyVariable - a model defined in Swagger"""  # noqa: E501
        super(StudyVariable, self).__init__(element_type="StudyVariable", **kwargs)
        self._name = None
        self._assay_refs = None
        self._average_function = None
        self._variation_function = None
        self._description = None
        self._factors = None
        self.discriminator = 'element_type'

        self.name = name
        if assay_refs is not None:
            self.assay_refs = assay_refs
        if average_function is not None:
            self.average_function = average_function
        if variation_function is not None:
            self.variation_function = variation_function
        if description is not None:
            self.description = description
        if factors is not None:
            self.factors = factors

    @property
    def name(self):
        """Gets the name of this StudyVariable.  # noqa: E501

        The study variable name.  # noqa: E501

        :return: The name of this StudyVariable.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StudyVariable.

        The study variable name.  # noqa: E501

        :param name: The name of this StudyVariable.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def assay_refs(self):
        """Gets the assay_refs of this StudyVariable.  # noqa: E501

        The assays referenced by this study variable.  # noqa: E501

        :return: The assay_refs of this StudyVariable.  # noqa: E501
        :rtype: list[Assay]
        """
        return self._assay_refs

    @assay_refs.setter
    def assay_refs(self, assay_refs):
        """Sets the assay_refs of this StudyVariable.

        The assays referenced by this study variable.  # noqa: E501

        :param assay_refs: The assay_refs of this StudyVariable.  # noqa: E501
        :type: list[Assay]
        """

        self._assay_refs = assay_refs

    @property
    def average_function(self):
        """Gets the average_function of this StudyVariable.  # noqa: E501

        The function used to calculate summarised small molecule quantities over the assays referenced by this study variable.  # noqa: E501

        :return: The average_function of this StudyVariable.  # noqa: E501
        :rtype: Parameter
        """
        return self._average_function

    @average_function.setter
    def average_function(self, average_function):
        """Sets the average_function of this StudyVariable.

        The function used to calculate summarised small molecule quantities over the assays referenced by this study variable.  # noqa: E501

        :param average_function: The average_function of this StudyVariable.  # noqa: E501
        :type: Parameter
        """

        self._average_function = average_function

    @property
    def variation_function(self):
        """Gets the variation_function of this StudyVariable.  # noqa: E501

        The function used to calculate the variation of small molecule quantities over the assays referenced by this study variable.  # noqa: E501

        :return: The variation_function of this StudyVariable.  # noqa: E501
        :rtype: Parameter
        """
        return self._variation_function

    @variation_function.setter
    def variation_function(self, variation_function):
        """Sets the variation_function of this StudyVariable.

        The function used to calculate the variation of small molecule quantities over the assays referenced by this study variable.  # noqa: E501

        :param variation_function: The variation_function of this StudyVariable.  # noqa: E501
        :type: Parameter
        """

        self._variation_function = variation_function

    @property
    def description(self):
        """Gets the description of this StudyVariable.  # noqa: E501

        A free-form description of this study variable.  # noqa: E501

        :return: The description of this StudyVariable.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StudyVariable.

        A free-form description of this study variable.  # noqa: E501

        :param description: The description of this StudyVariable.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def factors(self):
        """Gets the factors of this StudyVariable.  # noqa: E501

        Parameters indicating which factors were used for the assays referenced by this study variable, and at which levels.  # noqa: E501

        :return: The factors of this StudyVariable.  # noqa: E501
        :rtype: list[Parameter]
        """
        return self._factors

    @factors.setter
    def factors(self, factors):
        """Sets the factors of this StudyVariable.

        Parameters indicating which factors were used for the assays referenced by this study variable, and at which levels.  # noqa: E501

        :param factors: The factors of this StudyVariable.  # noqa: E501
        :type: list[Parameter]
        """

        self._factors = factors

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

        if issubclass(IndexedElement, dict):
            for key, value in super.items():
                result[key] = value

        if issubclass(StudyVariable, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StudyVariable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
