import unittest


from 接口模块自动化.api.api_uesr_details import ApiUser
from parameterized import parameterized

from 接口模块自动化.tools.read_user_detailsjson import ReadJson


# 单个数据使用
# def get_data():
#     # ReadJson("login.json").read_json()
#     data = ReadJson("user_details.json").read_json()
#     # 新建空列表，读取json数据
#     arrs = [(data.get("url"),
#              data.get("headers"),
#              data.get("status_code"))]
#     return arrs

# 多数据使用
def get_datas():
    datas = ReadJson("user_details.json").read_json()
    arr = []
    for data in datas.values():
        arr.append((data.get("url"),
                    data.get("headers"),
                    data.get("status_code")))
    return arr


class TestUserDetails(unittest.TestCase):
    @parameterized.expand(get_datas())
    def test_user_details(self, url, headers, status_code):
        # url = "http://test.zaitakugeek.cn:8000/user/profile?uid=111579943374652448"
        #
        # headers = {
        #     "Content-Type": "application/json",
        #     "Authorization": "Token 1c0edb0cf33e815a48e7f07a3461987cd0cffcb3"
        # }
        r = ApiUser().api_details(url, headers)

        print(r.json())
        print(r,status_code)
        self.assertEqual(status_code, r.status_code)


if __name__ == '__main__':
    unittest.main()
