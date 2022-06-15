from time import sleep

from parameterized import parameterized
import unittest
from 发布任务.base.get_driver import GetDriver
from 发布任务.page.page import PageLogin
from 发布任务.read_json.read_json import ReadJson


def get_data():
    datas = ReadJson("task.json").read_json()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("title"),
                     data.get("min_money"),
                     data.get("max_money"),
                     data.get("want_day"),
                     data.get("people_sum"),
                     data.get("describe"),
                     data.get("result")))
    return arrs


class TestLogin(unittest.TestCase):

    login = None

    @classmethod
    def setUpClass(cls):
        # 实例化driver并获取
        cls.driver = GetDriver().get_driver()
        # 实例化 获取登录对象
        cls.login = PageLogin(GetDriver().get_driver())
        cls.login.page_task_btn()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(3)
        GetDriver.quit_driver()

    @parameterized.expand(get_data())
    def test_wind(self, title, min_money, max_money,want_day, people_sum, describe,result):
        self.login.page_task(title, min_money, max_money,want_day, people_sum, describe)
        # if self.login.page_titLe_err_text() is None:
        #     if self.login.page_field_err_text() is None:
        #         print("正常运行")
        #     else:
        #         msg = self.login.page_field_err_text()
        #         return msg
        # else:
        #     msg = self.login.page_field_err_text()
        #     return msg
        # print(self.login.page_err_text())
        msg = self.login.page_field_err_text()
        # ms = self.login.page_err_text()
        # print(ms)
        print(msg)
        try:
            self.assertEqual(result,self.login.page_err_text())
        except AssertionError:
            self.login.page_get_image()
            print("错误")
            raise





