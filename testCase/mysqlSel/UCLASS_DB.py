# -*- coding: utf-8 -*-
# /usr/bin/python/

from common.configDB_UC import MyDB_UC

sql = 'select * from student limit 5'
cursor_connect = MyDB_UC().connectDB()
cursor_execute = MyDB_UC().executeSQL(sql,cursor_connect)
data = MyDB_UC().get_all(cursor_execute)
print(data)