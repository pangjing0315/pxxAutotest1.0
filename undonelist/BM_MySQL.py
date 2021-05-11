import pymysql
from sshtunnel import SSHTunnelForwarder


# 传入实例名和sql，返回查询结果
def SSHMysql(DB, SQL):
    # 配置SSH连接
    server = SSHTunnelForwarder(
        ssh_address_or_host=('140.130.74.54', 4888),  # 指定ssh登录的跳转机的address
        ssh_username='***',  # 跳转机的用户
        ssh_password='***',  # 跳转机的密码
        local_bind_address=('127.0.0.1', 1268),  # 映射到本机的地址和端口
        remote_bind_address=('16.1.24.201', 61113))  # 数据库的地址和端口

    server.start()  # 启用SSH
    # 数据库账户信息设置
    db = pymysql.connect(
        host="rm-2zek76bq37074it82lo.mysql.rds.aliyuncs.com",  # 映射地址local_bind_address IP
        port=3306,  # 映射地址local_bind_address端口
        user="sqladmin",
        passwd="jNj8CJCglvcr68Wn",
        database='business_20201202',
        charset='utf8')

    cursor = db.cursor()
    cursor.execute(SQL.encode('utf8'))  # 执行SQL
    data = cursor.fetchall()  # 获取查询结果

    # 关闭数据库连接
    cursor.close()
    return data


if __name__ == "__main__":
    SQL = "SELECT * FROM class_discount;"
    SelectResult = SSHMysql('business_20201202', SQL)
