import unittest

from nose_parameterized import parameterized

from 创建新的计划.api.jihua_api import JiHuaApi
from 创建新的计划.read_json.read_jihua import ReadJson


def get():
    data = ReadJson("jihua.json").jihua()
    arr = []
    for datas in data.values():
        arr.append((datas.get("url"),
                    datas.get("headers"),
                    datas.get("data"),
                    datas.get("status_code")))
    return arr


class TestJiHua(unittest.TestCase):
    @parameterized.expand(get())
    def test_jihua(self, url, headers, data, status_code):
        # url = "http://test.zaitakugeek.cn:8000/order/new"
        # headers = {
        #     "Content-Type": "application/json",
        #     "Authorization": "Token 2dfc33e02dec5dfeaccbb309d151197bbaa0157f"
        # }
        # data = {
        #     "cooperation_id": "111684859007370272",
        #     "payer": {
        #         "avatar": "http://test.zaitakugeek.cn:8080/static/storage/1/files/images/avatar/U111579952525607968/e7039c76e11b3ce98e3cee3702df8994.jpg",
        #         "nickname": "在宅极客用户项目发布",
        #         "user": "15018248542@163.com"
        #     },
        #     "payee": {
        #         "avatar": "http://test.zaitakugeek.cn:8080/static/storage/1/files/images/avatar/U111579943374652448/2789201054bc33228618d204299f0d7e.png",
        #         "nickname": "在宅极客用户自由职业者",
        #         "user": "111579943374652448"
        #     },
        #     "price": "666",
        #     "message": "1",
        #     "name": "测试计划",
        #     "expire_date": "2022-02-22",
        #     "start_date": "2022-02-21"
        # }
        r = JiHuaApi().jihua_api(url, headers, data)
        self.assertEqual(status_code, r.status_code)
        print(r.json())
        print(r.status_code)


if __name__ == '__main__':
    unittest.main()
