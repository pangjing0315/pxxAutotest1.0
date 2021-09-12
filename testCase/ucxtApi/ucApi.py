#!/usr/bin/python3
# _*_coding:utf-8 _*_
'''
@Time: 2021/9/12  3:39 下午
@Author: pangjing
api接口封装
'''

from common import api_requests

#base_url = 'https://console-rd.pxxclass.com'

def uclogin():
    '''登录'''
    login = api_requests.api_requests('login')
    login.data = {
        'account': 18100000001,
        'password': '31546e296683c39f88e92ce12071b640',
        'isVaildCode': 'false',
    }
    login.headers = {
        'Content-Type': "application/json; charset=utf-8"
    }
    r = login()
    assert 200 == r.status_code
    return r.cookies

def uclogout(cookies):
    '''退出登录'''
    logout = api_requests('logout', cookies=cookies)
    logout.method = 'GET'
    r = logout()
    assert 200 == r.status_code
    return r.json()

def class_getclass(cookies):
    '''我的班级列表'''
    class_getclass = api_requests('class_getclass', cookies=cookies)
    class_getclass.headers = {
        'Content-Type': "application/json; charset=utf-8",
        'role-type': "9"
    }
    class_getclass.data = {
        "page": 1,
        "pageSize": 15,
        "state": 0
    }
    r = class_getclass()
    assert 200 == r.status_code
    return r.json


