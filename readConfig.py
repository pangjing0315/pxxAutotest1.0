# -*- coding: utf-8 -*-
#读取配置文件
import os,codecs
import configparser
import getpathInfo  #引入我们自己的写的获取路径的类

path = getpathInfo.get_Path()#调用实例化，还记得这个类返回的路径为C:\Users\songlihui\PycharmProjects\dkxinterfaceTest
config_path = os.path.join(path, 'config.ini')#这句话是在path路径下再加一级，最后变成C:\Users\songlihui\PycharmProjects\dkxinterfaceTest\config.ini
proDir = os.path.split(os.path.realpath(__file__))[0]
config = configparser.ConfigParser()#调用外部的读取配置文件的方法
config.read(config_path, encoding='utf-8')


class ReadConfig():
    def __init__(self):
        fd = open(config_path)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(config_path, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value
    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value
    def get_mydb(self, name):#写好，留以后备用。但是因为我们没有对数据库的操作，所以这个可以屏蔽掉
        value = config.get('DATABASE', name)
        return value


if __name__ == '__main__':#测试一下，我们读取配置文件的方法是否可用
    print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off'))
