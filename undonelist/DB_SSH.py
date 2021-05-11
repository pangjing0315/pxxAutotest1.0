# _*_ coding:utf-8 _*_
import pymysql
from sshtunnel import SSHTunnelForwarder

class DB_SSH:
    '''
    数据库所在远程服务器IP：IP_C
    数据库所在远程服务器端口：Port_C
    跳板机（通过ssh通道）所在服务器IP：IP_B
    跳板机（通过ssh通道）所在服务器I端口：Port_B（22默认）
    跳板机（通过ssh通道）所在服务器账号：username_B
    跳板机（通过ssh通道）所在服务器密码：password_B

    '''
    def __init__(self, dbname,sql):

        self.dbname = dbname
        self.server = SSHTunnelForwarder(
            ('IP_B', '192.168.24.1'),
            ssh_username='username_B',
            ssh_password='password_B',
            remote_bind_address=('IP_C','192.168.24.1'))

        self.server.start()
        self.conn = pymysql.connect(host='rm-2zek76bq37074it82lo.mysql.rds.aliyuncs.com',
                                    port=self.server.local_bind_port,
                                    user='sqladmin',
                                    password='jNj8CJCglvcr68Wn',
                                    db=self.dbname,
                                    charset='utf8')
        print('数据库连接成功！')
        self.cur = self.conn.cursor()
        print('游标设置成功！')

    def __del__(self):  # 析构函数，实例删除时触发
        self.cur.close()
        self.conn.close()
        self.server.stop()

    def query(self, sql):
        print('开始执行查询语句{}'.format(sql))
        self.cur.execute(sql)
        print('sql{}执行成功！'.format(sql))
        return self.cur.fetchall()

    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print('sql{}执行成功！'.format(sql))
        except Exception as e:
            print(str(e))
            self.conn.rollback()


if __name__ == '__main__':
    name = 'business_20201202'
    sql = "select * from class_discount "
    connect = DB_SSH(name,sql)
    print(connect.query())

