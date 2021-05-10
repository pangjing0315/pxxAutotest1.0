# -*- coding: utf-8 -*-


import requests
import json
from common.Log import logger
import http.client
http.client.HTTPConnection._http_vsn = 10
http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'

logger = logger

class RunMain():

    def send_post(self, url, data):# 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        result = requests.post(url=url, json=data)# 因为这里要封装post方法，所以这里的url和data值不能写死
        #res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)#转换字符串
        return result

    def send_get(self, url, data):
        result = requests.get(url=url, json=data)
        #res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return result

    def run_main(self, method, url=None, data=None):#定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, data)
            logger.info(str(result))
        elif method == 'get':
            result = self.send_get(url, data)
            logger.info(str(result))
        else:
            print("method值错误！！！")
            logger.info("method值错误！！！")
        return result
if __name__ == '__main__':#通过写死参数，来验证我们写的请求是否正确
    result = RunMain().run_main('post', 'https://class-rd.youke100.com/class_in/admin/user/login?account=18512106695&password=dc906dafa1a09770c564e00ffc043f22&isVaildCode=false', 'account=18512106695&password=dc906dafa1a09770c564e00ffc043f22&isVaildCode=false')
    print(result)