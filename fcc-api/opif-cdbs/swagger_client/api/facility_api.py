# coding: utf-8

"""
    OPIF Service Data API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class FacilityApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def facility_search_keyword_format_get(self, keyword, format, **kwargs):  # noqa: E501
        """Search  # noqa: E501

        Search  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.facility_search_keyword_format_get(keyword, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str keyword: (required)
        :param str format: json,  xml (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.facility_search_keyword_format_get_with_http_info(keyword, format, **kwargs)  # noqa: E501
        else:
            (data) = self.facility_search_keyword_format_get_with_http_info(keyword, format, **kwargs)  # noqa: E501
            return data

    def facility_search_keyword_format_get_with_http_info(self, keyword, format, **kwargs):  # noqa: E501
        """Search  # noqa: E501

        Search  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.facility_search_keyword_format_get_with_http_info(keyword, format, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str keyword: (required)
        :param str format: json,  xml (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keyword', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method facility_search_keyword_format_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'keyword' is set
        if ('keyword' not in params or
                params['keyword'] is None):
            raise ValueError("Missing the required parameter `keyword` when calling `facility_search_keyword_format_get`")  # noqa: E501
        # verify the required parameter 'format' is set
        if ('format' not in params or
                params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `facility_search_keyword_format_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'keyword' in params:
            path_params['keyword'] = params['keyword']  # noqa: E501
        if 'format' in params:
            path_params['format'] = params['format']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/facility/search/{keyword}.{format}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
