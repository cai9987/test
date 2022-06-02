import unittest

from parameterized import parameterized


class TestPara(unittest.TestCase):
    # 多个参数[("账号","密码"),("账号","密码")]
    @parameterized.expand([("15018248542", "123456"), ("15018248542@163.com", "123456")])
    def test_para(self, account, password):
        print(account, password)
