#!/usr/bin/python3
# _*_coding:utf-8 _*_
'''
@Time: 2021/9/12  7:40 下午
@Author: pangjing
'''
import time
import sys,json,requests,unittest
from common import Log
from testCase.ucxtApi import ucApi

logger =Log.logger

class getClassTestCase(unittest.TestCase):
    '''
    def setParameters(self, case_name, path, query, method):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name
    '''
    def setUp(self):
        """
        :return:
        """
        print(self.case_name+"测试开始前准备")
        self.checkResult()

    def checkResult(self):# 断言
        """
        check test result
        :return:
        测试我的班级查询接口
        """
        expected_results = ['PJ-测试']
        ids = [result['name'] for result in expected_results]
        count = 1
        while len(ids) > 0 or count < 15:
            r = ucApi.class_getclass()
            self.assertEqual(200, r.status_code)
            results = r.json()['results']
            print("results:%s" %results)
            logger.info('开始第%d次查询...' % count)
            #results['name'] = dict([x.values() for x in results['name']])
            if results not in expected_results:
                logger.warning('不在期望结果中： %s' % results)
                print(results)
            logger.info('第%d次查询结束...' % count)
            if results['name'] in ids:
                ids.pop(ids.index(results['name']))
            count += 1
            time.sleep(1)

    def tearDown(self):
        #ucApi.uclogout(self.cookies)
        print("测试结束，输出log完结\n\n")