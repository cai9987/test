"""
    实现登录接口的对象封装
"""

# 导包
import requests
import json


# 新建类，对象接口
class ApiPhoneLogin(object):
    # 登录方法
    def api_post_login(self,url,verify_code, phone,region_code):
        url = "http://test.zaitakugeek.cn:8000/user/phone_login"
        headers = {
            "Content-Type": "application/json",
        }
        data = {
            "verify_code": verify_code,
            "phone": phone,
            "region_code": region_code
        }

        r = requests.post(url=url, json=data, headers=headers)
        return r
