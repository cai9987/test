import unittest

import requests
from nose_parameterized import parameterized

from 获取自己收到的合作申请.api.api_received import ApiReceived
from 获取自己收到的合作申请.tool.read_received import ReadJson


def get_data():
    datas = ReadJson("received.json").read_json()
    arr = []
    for data in datas.values():
        arr.append((data.get("url"),
                    data.get("headers"),
                    data.get("data"),
                    data.get("status_code")))
    return arr


class TestReceivedWork(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_received_work(self,url,headers,data,status_code):
        # url = "http://test.zaitakugeek.cn:8000/cooperation/provided_cooperation_list"
        # headers = {
        #     "Content-Type": "application/json",
        #     "Authorization": "Token 1c0edb0cf33e815a48e7f07a3461987cd0cffcb3"
        # }
        # data = {
        #     "start_date": "2022-01-07",
        #     "end_date": "2022-2-7"
        # }

        r = ApiReceived().api_received_work(url,headers,data)
        print(r.json())
        print(r.status_code)
        try:
            self.assertEqual(status_code, r.status_code)
        except AssertionError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
