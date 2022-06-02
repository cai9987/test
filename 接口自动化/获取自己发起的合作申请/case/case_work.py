import unittest
from 获取自己发起的合作申请.api.api_work import ApiWork
from parameterized import parameterized

from 获取自己发起的合作申请.tools.read_work import ReadJson


def get_data():
    datas = ReadJson("work.json").read_proposal()
    arr = []
    for data in datas.values():
        arr.append((data.get("url"),
                    data.get("headers"),
                    data.get("status_code")))
    return arr


class TestUserWork(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_work(self, url, headers, status_code):
        # url = "http://test.zaitakugeek.cn:8000/user/profile?uid=111579943374652448"
        #
        # headers = {
        #     "Content-Type": "application/json",
        #     "Authorization": "Token 1c0edb0cf33e815a48e7f07a3461987cd0cffcb3"
        # }
        r = ApiWork().api_work(url, headers)

        print(r.json())
        print(r,status_code)
        self.assertEqual(status_code, r.status_code)


if __name__ == '__main__':
    unittest.main()
