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
from swagger_client.models.parameter import Parameter  # noqa: F401,E501


class Instrument(object):
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
        'name': 'Parameter',
        'source': 'Parameter',
        'analyzer': 'list[Parameter]',
        'detector': 'Parameter'
    }

    attribute_map = {
        'name': 'name',
        'source': 'source',
        'analyzer': 'analyzer',
        'detector': 'detector'
    }

    def __init__(self, name=None, source=None, analyzer=None, detector=None):  # noqa: E501
        """Instrument - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._source = None
        self._analyzer = None
        self._detector = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if source is not None:
            self.source = source
        if analyzer is not None:
            self.analyzer = analyzer
        if detector is not None:
            self.detector = detector

    @property
    def name(self):
        """Gets the name of this Instrument.  # noqa: E501


        :return: The name of this Instrument.  # noqa: E501
        :rtype: Parameter
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Instrument.


        :param name: The name of this Instrument.  # noqa: E501
        :type: Parameter
        """

        self._name = name

    @property
    def source(self):
        """Gets the source of this Instrument.  # noqa: E501


        :return: The source of this Instrument.  # noqa: E501
        :rtype: Parameter
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Instrument.


        :param source: The source of this Instrument.  # noqa: E501
        :type: Parameter
        """

        self._source = source

    @property
    def analyzer(self):
        """Gets the analyzer of this Instrument.  # noqa: E501


        :return: The analyzer of this Instrument.  # noqa: E501
        :rtype: list[Parameter]
        """
        return self._analyzer

    @analyzer.setter
    def analyzer(self, analyzer):
        """Sets the analyzer of this Instrument.


        :param analyzer: The analyzer of this Instrument.  # noqa: E501
        :type: list[Parameter]
        """

        self._analyzer = analyzer

    @property
    def detector(self):
        """Gets the detector of this Instrument.  # noqa: E501


        :return: The detector of this Instrument.  # noqa: E501
        :rtype: Parameter
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """Sets the detector of this Instrument.


        :param detector: The detector of this Instrument.  # noqa: E501
        :type: Parameter
        """

        self._detector = detector

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
        if not isinstance(other, Instrument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
        
    def to_lines(self):
        lines = []
        if self.name: lines += ['-name\t{}'.format(self.name.as_line())]
        if self.source: lines += ['-source\t{}'.format( self.name.as_line())]
        for idx, e in enumerate(self.analyzer,1):
            lines += ['-analyzer[{}]\t{}'.format( idx, e.as_line())]
        lines += ['-source\t{}'.format( self.name.as_line())]
        if self.detector: lines += ['-detector\t{}'.format('-detector', self.name.as_line())]
#         'source': 'Parameter',
#         'analyzer': 'list[Parameter]',
#         'detector': 'Parameter'
        return lines

    @staticmethod
    def fromText(lines):
        if not lines: return None
        import re
        name_li = None
        source_li = None
        analyzer_li = None
        detector_li = None
        
        for l in lines:
            if l.startswith('-name'):
                name_li = re.match('-name\t(.*)', l).group(1)
            if l.startswith('-source'):
                source_li = re.match('-source\t(.*)', l).group(1)
            if l.startswith('-analyzer'):
                if not analyzer_li: analyzer_li = []
                analyzer_li.append(l)
            if l.startswith('-detector'):
                detector_li = re.match('-detector\t(.*)', l).group(1)
        
        analyzer = None
        for l in analyzer_li:
            parameter_li = re.match('-analyzer\[\d+\](.*)', l).group(1).strip()
            if not analyzer: analyzer = []
            analyzer.append(Parameter.fromText(parameter_li))
            
        
        kwargs = {
        'name': Parameter.fromText(name_li),
        'source': Parameter.fromText(source_li),
        'analyzer': analyzer,
        'detector': Parameter.fromText(detector_li)
        }
        return Instrument(**kwargs)