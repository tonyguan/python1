# coding=utf-8
# 代码文件：chapter24/QQ2006/com/zhijieketang/qq/server/base_dao.py

"""定义DAO基类"""
import pymysql
import configparser
import logging

logger = logging.getLogger(__name__)

class BaseDao(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini', encoding='utf-8')

        host = self.config['db']['host']
        user = self.config['db']['user']
        # 读取整数port数据
        port = self.config.getint('db', 'port')
        password = self.config['db']['password']
        database = self.config['db']['database']
        charset = self.config['db']['charset']

        self.conn = pymysql.connect(host=host,
                                    user=user,
                                    port=port,
                                    password=password,
                                    database=database,
                                    charset=charset)

    def close(self):
        """关闭数据库连接"""

        self.conn.close()
