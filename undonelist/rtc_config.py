import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from sshtunnel import SSHTunnelForwarder
import requests

method = "post"
url = 'console-rd.pxxclass.com/'
#https://console-rd.pxxclass.com/class_in/admin/class/getclass

def rtc_config(url,method,json):
    with SSHTunnelForwarder(
            ssh_address_or_host=('192.168.1.249', 22),
            # ssh_pkey="D:\\Program Files\\my\\key\\pangjingg.pem",
            ssh_pkey="/Users/pangjing/Documents/My_work/pangjing.pem",
            ssh_private_key_password='Q43DlYKbFRZ_eRQm',
            ssh_username='pangjing',
            remote_bind_address=('192.168.8.41',2019)) as tunnel:
        a = tunnel.local_bind_port
        d = {
            'url' : url,
            'method': method,
            'json': json
        }
        r = requests.post("http://127.0.0.1:{}/transverter".format(a),json=d)

        str1=r.text.encode('utf-8').decode('unicode_escape')
        return str1

class work_script(object):
    '''
      def __init__(self, test_type="t", base_url='edps', method = "post"):
        self.url = rpc_url[test_type][base_url]
        self.method = method

    '''
    def __init__(self,url,method):
        self.url =url
        self.method = method

    def api_requests(self, url, json):
        '''
        公共调用请求方法，相当于requests.post
        :param url: 接收请求的拼接得url
        :param json: 接收请求的参数json值
        :return: 返回响应的文本
        '''
        return rtc_config(url, self.method, json)

    #班级查询
    def class_getclass(self):
        url = self.url + "class_in/admin/class/getclass"
        json ={
            #"tid":1170,
            "page": 1,
            "pageSize": 15,
            "state": 0,

        }
        return self.api_requests(url, json)

if __name__ == "__main__":
    d = work_script(url,method)
    print("************************查询推荐课程*******************************************************")
    print(d.class_getclass())