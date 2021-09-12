#!/usr/bin/python3
# _*_coding:utf-8 _*_
'''
@Time: 2021/9/12  5:20 下午
@Author: pangjing
'''

import requests

from common.api_requests import api_requests
from testCase.ucxtApi.ucApi import uclogin


cookies = uclogin()
class_getclass = api_requests('class_getclass', cookies=cookies)
class_getclass.headers = {
    'Content-Type': "application/json; charset=utf-8",
    'role-type': "9"
}
class_getclass.data = {
    "page":1,
    "pageSize":15,
    "state":0
}
print(class_getclass().json())