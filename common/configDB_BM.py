# -*- coding: utf-8 -*

import pymysql
from common import readConfig as readConfig
import common.Log as Log

localReadConfig = readConfig.ReadConfig()

class MyDB_BM:
    global host, username, password, port, database, config
    host = localReadConfig.get_mydb_bm("host")
    port = localReadConfig.get_mydb_bm("port")
    username = localReadConfig.get_mydb_bm("username")
    password = localReadConfig.get_mydb_bm("password")
    database = localReadConfig.get_mydb_bm("database")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database
    }

    def __init__(self):
        self.log = Log.Logger()
        self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None

    def connectDB(self):
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
        except ConnectionError as ex:
            self.logger.error(str(ex))
        #return self.cursor

    def executeSQL(self, sql, params):
        self.connectDB()
        # executing sql
        self.cursor.execute(sql, params)
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()
        print("Database closed!")
