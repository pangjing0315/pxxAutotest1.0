# -*- coding: utf-8 -*-
# /usr/bin/python/

from common.configDB import MyDB

sql = "select * from class_discount where class_id  limit 5"
cursor_connect = MyDB().connectDB()
cursor_execute = MyDB().executeSQL(sql,cursor_connect)
data = MyDB().get_all(cursor_execute)
print(data)