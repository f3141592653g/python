# -*- coding:utf-8 _*-
""" 
@author:zhouzongquan
@time: 2018/12/17
@email:919839065@qq.com
@function： 
"""
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # opfun_API路径

case_file = os.path.join(base_dir, 'data', 'cases.xlsx')  # cases文件路径

global_file = os.path.join(base_dir, 'config', 'global.conf')

online_file = os.path.join(base_dir, 'config', 'online.cfg')

test_file = os.path.join(base_dir, 'config', 'test.conf')

jdbc_file = os.path.join(base_dir, 'config', 'jdbc.cfg')

log_conf_file = os.path.join(base_dir, 'config', 'log_conf.cfg')

log_dir = os.path.join(base_dir, 'log')

case_dir = os.path.join(base_dir, 'testcases')

report_dir = os.path.join(base_dir, 'reports')


