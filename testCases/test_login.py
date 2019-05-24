# -*- coding:utf-8 _*-
""" 
@author:zhouzongquan
@time: 2018/12/17
@email:919839065@qq.com
@function：
"""

import unittest

from ddt import ddt, data

from opfun_API.common import do_excel
from opfun_API.common.logger import *
from opfun_API.common.http_request import HTTPRequest



@ddt
class LoginTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'login')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request = HTTPRequest()
        cls.http_request.logger.info('准备测试前置')

    @data(*cases)
    def test_login(self, case):
        self.http_request.logger.info('开始测试：{0}'.format(case.title))
        resp = self.http_request.request(case.method, case.url, case.data)

        try:
            self.assertEqual(case.expected, resp.text)
            self.excel.write_result(case.case_id + 1, resp.text, 'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, 'FAIL')
            self.http_request.logger.error("报错了，{0}".format(e))
            raise e
        self.http_request.logger.info('结束测试：{0}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        cls.http_request.logger.info('测试后置处理')
        cls.http_request.close()
