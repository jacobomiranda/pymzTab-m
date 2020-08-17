# coding: utf-8

"""
    mzTab-M reference implementation and validation API.

    This is the mzTab-M reference implementation and validation API service.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: nils.hoffmann@isas.de
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ValidatePlainApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def validate_plain_mz_tab_file(self, mztabfile, **kwargs):  # noqa: E501
        """validate_plain_mz_tab_file  # noqa: E501

        Validates an mzTab file in plain text representation / tab-separated format and reports syntactic, structural, and semantic errors.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_plain_mz_tab_file(mztabfile, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str mztabfile: mzTab file that should be validated. (required)
        :param str level: The level of errors that should be reported, one of ERROR, WARN, INFO.
        :param int max_errors: The maximum number of errors to return.
        :param bool semantic_validation: Whether a semantic validation against the default rule set should be performed.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ValidationMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.validate_plain_mz_tab_file_with_http_info(mztabfile, **kwargs)  # noqa: E501

    def validate_plain_mz_tab_file_with_http_info(self, mztabfile, **kwargs):  # noqa: E501
        """validate_plain_mz_tab_file  # noqa: E501

        Validates an mzTab file in plain text representation / tab-separated format and reports syntactic, structural, and semantic errors.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_plain_mz_tab_file_with_http_info(mztabfile, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str mztabfile: mzTab file that should be validated. (required)
        :param str level: The level of errors that should be reported, one of ERROR, WARN, INFO.
        :param int max_errors: The maximum number of errors to return.
        :param bool semantic_validation: Whether a semantic validation against the default rule set should be performed.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ValidationMessage], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'mztabfile',
            'level',
            'max_errors',
            'semantic_validation'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_plain_mz_tab_file" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'mztabfile' is set
        if self.api_client.client_side_validation and ('mztabfile' not in local_var_params or  # noqa: E501
                                                        local_var_params['mztabfile'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `mztabfile` when calling `validate_plain_mz_tab_file`")  # noqa: E501

        if self.api_client.client_side_validation and 'max_errors' in local_var_params and local_var_params['max_errors'] > 500:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `max_errors` when calling `validate_plain_mz_tab_file`, must be a value less than or equal to `500`")  # noqa: E501
        if self.api_client.client_side_validation and 'max_errors' in local_var_params and local_var_params['max_errors'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `max_errors` when calling `validate_plain_mz_tab_file`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'level' in local_var_params and local_var_params['level'] is not None:  # noqa: E501
            query_params.append(('level', local_var_params['level']))  # noqa: E501
        if 'max_errors' in local_var_params and local_var_params['max_errors'] is not None:  # noqa: E501
            query_params.append(('maxErrors', local_var_params['max_errors']))  # noqa: E501
        if 'semantic_validation' in local_var_params and local_var_params['semantic_validation'] is not None:  # noqa: E501
            query_params.append(('semanticValidation', local_var_params['semantic_validation']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'mztabfile' in local_var_params:
            body_params = local_var_params['mztabfile']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['text/tab-separated-values', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/validatePlain', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ValidationMessage]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
