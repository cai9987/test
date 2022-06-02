import unittest
from time import sleep

from selenium import webdriver


class Test01(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        url = "http://test.zaitakugeek.cn:8080/home/index"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        sleep(2)
        self.driver.close()

    def test01(self):
        self.driver.find_element_by_css_selector(".el-menu-item.login-btn.login-btn-only>div").click()
        self.driver.find_element_by_xpath("html/body/div[1]/div[2]/div[2]/form/div/div[1]/div/div/input").send_keys(
            "15018248542")
        self.driver.find_element_by_xpath("html/body/div[1]/div[2]/div[2]/form/div/div[2]/div/div/input").send_keys("")
        self.driver.find_element_by_css_selector(".el-checkbox__inner").click()
        self.driver.find_element_by_css_selector(".slide-verify-slider-mask-item-icon").click()
        sleep(10)

        result = self.driver.find_element_by_css_selector(".el-message__content").text
        print(result)
        expect_result = "验证不通过，请再次验证！"

        try:
            self.assertEqual(expect_result,result)
            
        except AssertionError:

            self.driver.get_screenshot_as_file("./image/login_error.png")
