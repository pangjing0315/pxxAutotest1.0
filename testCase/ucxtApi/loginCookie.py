#!/usr/bin/python3
# _*_coding:utf-8 _*_
'''
@Time: 2021/9/12  4:39 下午
@Author: pangjing
获取登录的cookie值
'''

import requests
from testCase.ucxtApi.ucApi import uclogin

print('login......')
cookies = uclogin()
print("cookies: %s" %cookies)

'''
#------再次访问url打印headers验证cookies是否正确---------
base_url = 'https://console-rd.pxxclass.com'
url = base_url + '/class_in/admin/user/login?account=18100000001&password=31546e296683c39f88e92ce12071b640&isVaildCode=falsen'
r = requests.post(url, cookies=cookies)
print(r.request.url)
print(r.request.headers)

'''

