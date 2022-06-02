import unittest

from nose_parameterized import parameterized

from 获取指定需求详情.api.demand_api import DemandApi
from 获取指定需求详情.read_json.read_demand import ReadJson


def get_i():
    data = ReadJson("demand.json").read_proposal()
    arr = []
    for i in data.values():
        arr.append((i.get("url"),
                    i.get("headers"),
                    i.get("params"),
                    i.get("status_code")))
    return arr


class TestDemand(unittest.TestCase):
    @parameterized.expand(get_i())
    def test_demand(self, url, headers, params, status_code):
        # url = "http://test.zaitakugeek.cn:8000/hire/info"
        # headers = {"Content-Type": "application/json",
        #            "Authorization": "Token 1c0edb0cf33e815a48e7f07a3461987cd0cffcb3"}
        # params = {"demand_id": "111667862747350048"}
        r = DemandApi().demand_api(url, headers, params)
        print(r.json())
        try:
            self.assertEqual(status_code, r.status_code)
        except:
            raise


if __name__ == '__main__':
    unittest.main()
