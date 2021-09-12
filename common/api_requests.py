#!/usr/bin/python3
# _*_coding:utf-8 _*_
'''
@Time: 2021/9/12  3:28 下午
@Author: pangjing
api请求封装
'''

import sys
import requests
from common import Log, configUrlApi
from common.configUrlApi import *
from testCase.ucxtApi import ucApi

logger =Log.logger

class api_requests(object):

    def __init__(self, name, platform='t', data=None, headers=None, method='POST', timeout=10, cookies=None,
                 files=None):
        self.name = name
        self.platform = platform
        self.headers = headers or {}
        self.data = data or {}
        self.method = method.upper()
        self.timeout = timeout
        self.cookies = cookies
        self.files = files

    @property
    def url(self):
        return configUrlApi.bmUrl['base_url'][self.platform][self.name] + configUrlApi.bmUrl['apis'][self.name]

    @property
    def requests_kwargs(self):
        if self.method == 'POST':
            if 'Content-Type' in self.headers.keys() and 'application/json' in self.headers['Content-Type']:
                return {
                    'json': self.data,
                    'headers': self.headers,
                    'timeout': self.timeout,
                    'cookies': self.cookies,
                    'files': self.files
                }
            else:
                return {
                    'data': self.data,
                    'headers': self.headers,
                    'timeout': self.timeout,
                    'cookies': self.cookies,
                    'files': self.files
                }
        else:
            return {
                'params': self.data,
                'headers': self.headers,
                'timeout': self.timeout,
                'cookies': self.cookies,
                'files': self.files
            }


    def __call__(self, **kwargs):
        try:
            r = requests.request(self.method, self.url, **self.requests_kwargs, **kwargs)
            return r
        except TimeoutError as e:
            logger.error('%s timeout' % self.name)
            sys.exit(0)
