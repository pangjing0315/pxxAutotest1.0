# -*- coding: utf-8 -*-
#获取项目绝对路径

import os

def get_Path_a():
    #path = os.path.split(os.path.realpath(__file__))[0]
    path =os.path.split('/Users/pj/PycharmProjects/pxxAutotest1.0/runAllmain.py')[0]
    return path

def get_Path_b():
    path = os.path.split(os.path.realpath(__file__))[0]
    #path =os.path.split('/Users/pj/PycharmProjects/pxxAutotest1.0/runAllmain.py')[0]
    return path

if __name__ == '__main__':# 执行该文件，测试下是否OK
    get_Path_a()
    get_Path_b()
    #print('测试路径是否OK,路径为：', get_Path_a())
    #print('测试路径是否OK,路径为：', get_Path_b())

