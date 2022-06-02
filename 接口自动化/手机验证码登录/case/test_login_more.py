import unittest
# 导入登录函数调用
from 手机验证码登录.api.api_login import ApiPhoneLogin
from parameterized import parameterized
from 手机验证码登录.tools.read_json import ReadJson


def get_data():
    datas = ReadJson("login_more.json").read_json()
    # 新建空列表，读取json数据
    arrs = []
    # 使用遍历获取所有的value
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("verify_code"),
                     data.get("phone"),
                     data.get("region_code"),
                     data.get("status_code")))
    return arrs


class TestLogin(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_login(self,url, verify_code, phone, region_code, status_code):
        # url = "http://test.zaitakugeek.cn:8000/user/email_login"
        # account = "15018248542@163.com"
        # password = "123456"

        # 调用函数
        s = ApiPhoneLogin().api_post_login(url,verify_code, phone, region_code)
        # print("返回数据：", s.json())
        print(s.status_code)
        # 断言
        assert s.json()['uid'] == '111579943374652448'
        try:
            # 断言
            self.assertEqual('1c0edb0cf33e815a48e7f07a3461987cd0cffcb3', s.json()['token'])
        except AssertionError as e:
            print(e)
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
