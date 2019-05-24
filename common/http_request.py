# -*- coding:utf-8 _*-
""" 
@author:zhouzongquan
@time: 2018/12/17
@email:919839065@qq.com
@function： 
"""
import requests

from opfun_API.common.config import config
from opfun_API.common.logger import *


class HTTPRequest:
    """
        公共使用一个session, cookies自动传递
       使用这类的request方法去完成不同的HTTP请求，并且返回响应结果
    """
    logger = Logger("py15").get_logger()

    def __init__(self):
        # 打开一个session
        self.session = requests.sessions.session()

    def request(self, method, url, data=None, json=None):
        method = method.upper()  # 将method强制转成全大小

        if type(data) == str:
            data = eval(data)  # str转成字典

        # 拼接URL
        url = config.get('api', 'pre_url') + url
        self.logger.debug('请求url:{0}'.format(url))
        self.logger.debug('请求data:{0}'.format(data))

        if method == 'GET':
            resp = self.session.request(method=method, url=url, params=data)
        elif method == 'POST':
            if json:
                resp = self.session.request(method=method, url=url, json=json)
            else:
                resp = self.session.request(method=method, url=url, data=data)
        else:
            resp = None
            self.logger.error('UN-support method')

        self.logger.debug('请求response:{0}'.format(resp.text))
        return resp

    def close(self):
        self.session.close()  # 用完关闭



# if __name__ == '__main__':
#     ht = HTTPRequest().request("POST","user/passwd_smscode_login",data={"phone":"18668208137","password":"123qwe"}).status_code
#     print(ht)