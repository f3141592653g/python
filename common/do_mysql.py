# -*- coding:utf-8 _*-
"""
@author:zhouzongquan
@time: 2018/12/17
@email:919839065@qq.com
@function：
"""
import pymysql
from opfun_API import config


class DoMysql:
    """
    完成与MySQL数据库的一个交互
    """

    def __init__(self):
        # 把这些参数放到配置文件里面去做，然后在这里读取配置文件

        cf = config()
        host = cf.get("connect", "host")
        user = cf.get("connect", "user")
        password = cf.get("connect", "password")
        port = int(cf.get("connect", "port"))

        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port, charset='utf8')
        # 设置返回字典
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)  # 创建游标

    def fetch_one(self, sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()  # 返回一条数据，元组

    def fetch_all(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()  # 返回多条数据的时候，元组里面套元组

    def close(self):
        self.cursor.close()  # 关闭游标
        self.mysql.close()  # 关闭连接
