import unittest
from selenium import webdriver
from time import sleep


class TestWind(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        url = "http://47.107.116.139/phpwind/index.php?m=bbs"
        self.driver.get(url)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()

    def test_wind(self):
        # self.driver.find_element_by_css_selector(".header_login>a").click()
        self.driver.add_cookie({"name": "csrf_token", "value": "bd5ab2585f4aaeb8"})
        sleep(3)
        self.driver.refresh()
        sleep(8)
