from time import sleep

from parameterized import parameterized
import unittest

from 登录模块.base.get_driver import GetDriver
from 登录模块.page.page import PageLogin
from 登录模块.read_json.read_json import ReadJson


def get_data():
    datas = ReadJson("sign.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("username"),
                     data.get("password"),
                     data.get("result"),
                     data.get("flag"),
                     data.get("num")))
    return arrs


class TestLogin(unittest.TestCase):

    login = None

    @classmethod
    def setUpClass(cls):
        # 实例化driver并获取
        cls.driver = GetDriver().get_driver()
        # 实例化 获取登录对象
        cls.login = PageLogin(GetDriver().get_driver())

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(3)
        GetDriver.quit_driver()

    @parameterized.expand(get_data())
    def test_wind(self, username, password, result, flag, num):
        self.login.page_login(username, password)
        if flag is False:
            if num == 1:
                msg = self.login.page_err_up_text()
                print(msg)
                try:
                    self.assertEqual(result, self.login.page_err_up_text())
                except AssertionError:
                    self.login.page_get_image()
                    raise
            elif num == 2:
                msg = self.login.page_err_username_text()
                print(msg)
                try:
                    self.assertEqual(result, self.login.page_err_username_text())
                except AssertionError:
                    self.login.page_get_image()
                    raise
            elif num == 3:
                msg = self.login.page_err_password_text()
                print(msg)
                try:
                    self.assertEqual(result, self.login.page_err_password_text())
                except AssertionError:
                    self.login.page_get_image()
                    raise
            else:
                print("没有问题")
        else:
            self.login.page_if_success()

