# -*- coding:utf-8 _*-
""" 
@author:zhouzongquan
@time: 2018/12/17 
@email:919839065@qq.com
@function： 
"""
import configparser
from opfun_API.common import contants


class ReadConfig:
    """
    完成配置文件的读取
    """

    def __init__(self, encoding='utf-8'):
        self.config = configparser.ConfigParser()
        self.encoding = encoding
        self.config.read(contants.global_file, encoding)  # 先加载global
        self.config.read(contants.jdbc_file, encoding)
        self.config.read(contants.log_conf_file, encoding)
        switch = self.config.getboolean('switch', 'on')
        if switch:  # 开关打开的时候，使用online的配置
            self.config.read(contants.online_file, encoding)
        else:  # 开关关闭的时候，使用test的配置
            self.config.read(contants.test_file, encoding)

    def get(self, section, option):
        return self.config.get(section, option)


config = ReadConfig()

#
# if __name__ == '__main__':
#     print(contants.log_conf_file)
#     log_lv = ReadConfig().get("log", "logger_level")
#     print(log_lv)