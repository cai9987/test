import unittest

import requests
from parameterized import parameterized

from 获取用户信息.api.user_api import TestUser
from 获取用户信息.read_json.read_user_json import ReadJson


def get_data():
    datas = ReadJson("use.json").read_uesr_json()
    arr = []
    for data in datas.values():
        arr.append((data.get("headers"),
                    data.get("params"),
                    data.get("url"),
                    data.get("status_code")))
    return arr


class TestUserCase(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_user(self, headers, params, url, status_code):
        # headers = {
        #     "Content-Type": "application/json",
        #     "Authorization": "Token 0f3f4f9e398819eb92f6dae3abe7958c50670338"
        # }
        # params = {"uid": "111579943374652448"}
        # url = "http://test.zaitakugeek.cn:8000/user/profile"
        r = TestUser().user_api(headers, params, url)
        # r = requests.get(headers=headers,url=url,params=params)
        print(r.json())
        print(r.status_code)
        try:
            self.assertEqual(status_code, r.status_code)
        except AssertionError:
            raise


if __name__ == '__main__':
    TestUserCase().test_user()
