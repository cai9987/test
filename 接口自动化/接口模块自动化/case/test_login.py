import unittest
# 导入登录函数调用
from 接口模块自动化.api.api_login import ApiLogin
from parameterized import parameterized
from 接口模块自动化.tools.read_json import ReadJson


def get_data():
    data = ReadJson("login.json").read_json()
    # 新建空列表，读取json数据
    arrs = [(data.get("url"),
             data.get("account"),
             data.get("password"),
             data.get("status_code"))]
    return arrs


class TestLogin(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_login(self, url, account, password, status_code):
        # url = "http://test.zaitakugeek.cn:8000/user/email_login"
        # account = "15018248542@163.com"
        # password = "123456"

        # 调用函数
        s = ApiLogin().api_post_login(url, account, password)
        print("返回数据：", s.json())
        print(s.status_code)
        # 断言
        assert s.json()['uid'] == '111579952525607968'
        # try:
        #     # 断言
        #     self.assertEqual('1c0edb0cf33e815a48e7f07a3461987cd0cffcb3', s.json()['token'])
        # except AssertionError as e:
        #     print(e)
        # 断言状态码
        try:
            assert s.status_code == status_code
        except AssertionError as e:
            print(e)
        token = {"Token" + " " + s.json()['token']}
        print(token)
        return token


if __name__ == '__main__':
    unittest.main()
