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


class Database(object):
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
        'param': 'Parameter',
        'prefix': 'str',
        'version': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'param': 'param',
        'prefix': 'prefix',
        'version': 'version',
        'uri': 'uri'
    }

    def __init__(self, param=None, prefix=None, version=None, uri=None):  # noqa: E501
        """Database - a model defined in Swagger"""  # noqa: E501

        self._param = None
        self._prefix = None
        self._version = None
        self._uri = None
        self.discriminator = None

        self.param = param
        self.prefix = prefix
        self.version = version
        self.uri = uri

    @property
    def param(self):
        """Gets the param of this Database.  # noqa: E501


        :return: The param of this Database.  # noqa: E501
        :rtype: Parameter
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this Database.


        :param param: The param of this Database.  # noqa: E501
        :type: Parameter
        """
        if param is None:
            raise ValueError("Invalid value for `param`, must not be `None`")  # noqa: E501

        self._param = param

    @property
    def prefix(self):
        """Gets the prefix of this Database.  # noqa: E501


        :return: The prefix of this Database.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this Database.


        :param prefix: The prefix of this Database.  # noqa: E501
        :type: str
        """
        if prefix is None:
            raise ValueError("Invalid value for `prefix`, must not be `None`")  # noqa: E501

        self._prefix = prefix

    @property
    def version(self):
        """Gets the version of this Database.  # noqa: E501


        :return: The version of this Database.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Database.


        :param version: The version of this Database.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def uri(self):
        """Gets the uri of this Database.  # noqa: E501


        :return: The uri of this Database.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Database.


        :param uri: The uri of this Database.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

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
        if not isinstance(other, Database):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    def to_lines(self):
#         'param': 'Parameter',
#         'prefix': 'str',
#         'version': 'str',
#         'uri': 'str'

        lines = []
        if self.param: lines += ['\t{}'.format(self.param.as_line())]
        if self.prefix: lines += ['-prefix\t{}'.format(self.prefix)]
        if self.version: lines += ['-version\t{}'.format(self.version)]
        if self.uri: lines += ['-uri\t{}'.format(self.uri)]
                                          
        return lines
    
    @staticmethod
    def fromText(lines):
        import re
        
        def sanitize(item):
            if isinstance(item, str):
                item = item.strip()
            
            if item is None or len(item) == 0:
                return None
            
            return item
        
        for l in lines:
            if l.startswith('-prefix'):
                prefix = re.match('-prefix\t(.*)', l).group(1)
            elif l.startswith('-version'):
                version = re.match('-version\t(.*)', l).group(1)
            elif l.startswith('-uri'):
                uri = re.match('-uri\t(.*)', l).group(1)
            else:
                param = l
       
        kwargs = {
        'param': Parameter.fromText(param),
        'prefix': sanitize(prefix),
        'version': sanitize(version),
        'uri': sanitize(uri)
        }
        return Database(**kwargs)