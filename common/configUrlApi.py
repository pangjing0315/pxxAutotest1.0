#!/usr/bin/python3
# _*_coding:utf-8 _*_
'''
@Time: 2021/9/12  3:10 下午
@Author: pangjing
公共Url和apis维护文件
'''

bmUrl = {
    'universal': ('login', 'logout', 'class_getclass', 'course_list'),
    'base_url': {
        't': {
            'login': 'https://console-rd.pxxclass.com',
            'logout': 'https://console-rd.pxxclass.com',
            'class_getclass': 'https://console-rd.pxxclass.com',
            'course_list': 'https://console-rd.pxxclass.com'
        },
        'f': {
            'login': 'https://console.pxxclass.com',
            'logout': 'https://console.pxxclass.com',
            'class_getclass': 'https://console.pxxclass.com',
            'course_list': 'https://console.pxxclass.com'
        }
    },
    'apis': {
        'login': '/class_in/admin/user/login?account=18100000001&password=31546e296683c39f88e92ce12071b640&isVaildCode=falsen',
        'logout': '',
        'class_getclass': '/class_in/admin/class/getclass',
        'course_list': '/class_in/admin/course/list'
    }
}
