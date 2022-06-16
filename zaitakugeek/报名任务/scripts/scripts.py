from time import sleep

from parameterized import parameterized
import unittest

from 报名任务.base.get_driver import GetDriver
from 报名任务.page.page import PageLogin
from 报名任务.read_json.read_json import ReadJson


def get_data():
    datas = ReadJson("sign.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("task_want_time"),
                     data.get("task_want_money"),
                     data.get("task_dir"),
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
    def test_wind(self, task_sign, task_want_time, task_want_money, result, flag, num):
        self.login.page_task_ok(task_sign, task_want_time, task_want_money)
        if flag is False:
            if num == 1:
                msg = self.login.page_time_err_text()
                print(msg)
                try:
                    self.assertEqual(result, self.login.page_time_err_text())
                except AssertionError:
                    self.login.page_get_image()
                    raise
            elif num == 2:
                msg = self.login.page_money_err_text()
                print(msg)
                try:
                    self.assertEqual(result, self.login.page_money_err_text())
                except AssertionError:
                    self.login.page_get_image()
                    raise
            else:
                print("没有问题")
        else:
            print("成功")


if __name__ == '__main__':
    TestLogin()
