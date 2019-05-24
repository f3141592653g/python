# -*- coding:utf-8 _*-
""" 
@author:zhouzongquan
@time: 2018/12/17
@email:919839065@qq.com
@function： 
"""

import logging

from opfun_API.common import contants
from opfun_API.common.config import ReadConfig


class Logger:
    def __init__(self, log_collector, encoding="utf-8"):
        self.log_collector = log_collector
        self.encoding = encoding

        # self.my_logger = logging.getLogger(log_collector)
        # self.file_log = logging.FileHandler(contants.log_dir + '/case.log')  # 指定输出到py15.log日志文件
        # self.channel = logging.StreamHandler()  # 指定输出到控制台

    def get_logger(self):
        log_lv = ReadConfig().get("log", "logger_level")
        log_msg = ReadConfig().get("log", "logger_fmt")
        my_logger = logging.getLogger(self.log_collector)  # 创建一个日志收集器
        my_logger.setLevel(log_lv)

        fmt = logging.Formatter(log_msg)

        channel = logging.StreamHandler()  # 指定输出到控制台
        channel.setLevel(log_lv)
        channel.setFormatter(fmt)  # 格式化输出

        file_log = logging.FileHandler(contants.log_dir + '/case.log')  # 指定输出到py15.log日志文件
        file_log.setLevel(log_lv)
        file_log.setFormatter(fmt)

        my_logger.addHandler(channel)
        my_logger.addHandler(file_log)

        file_log.close()
        return my_logger
#
#
# if __name__ == '__main__':
#     logger = Logger('case').get_logger()
#     logger.info('测试开始啦')
#     logger.error('测试报错')
#     logger.debug('测试数据')
#     logger.info('测试结束')
