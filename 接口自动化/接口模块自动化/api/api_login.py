"""
    实现登录接口的对象封装
"""

# 导包
import requests
import json


# 新建类，对象接口
class ApiLogin(object):
    # 登录方法
    def api_post_login(self, url, account, password):
        headers = {
            "Content-Type": "application/json",
        }
        data = {
            "account": account,
            "password": password
        }

        r = requests.post(url=url, json=data, headers=headers)
        return r
