# -*- coding: utf-8 -*-
# /usr/bin/python/

from common.configDB_BM import MyDB_BM

sql = 'select * from class_discount limit 5'
cursor_connect = MyDB_BM().connectDB()
cursor_execute = MyDB_BM().executeSQL(sql,cursor_connect)
data = MyDB_BM().get_all(cursor_execute)
print(data)