import unittest
from selenium import webdriver


class Test01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "http://47.107.116.139/phpwind/index.php?m=bbs"
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test01(self):
        self.driver.find_element_by_css_selector(".header_login>a").click()
        self.driver.find_element_by_css_selector("#J_u_login_username").send_keys("jiasuo")
        self.driver.find_element_by_css_selector("#J_u_login_password").send_keys("")
        self.driver.find_element_by_css_selector(".btn.btn_big.btn_submit.mr20").click()
        # 获取登录后信息
        result = self.driver.find_element_by_css_selector(".tips_icon_error").text
        print(result)
        # 定义预期结果
        # expect_result = "密码不能为空"
        expect_result = "密码不能为空!"
        try:
            # 断言
            self.assertEqual(expect_result, result)
        except AssertionError:
            # 截图
            print("截图")
            self.driver.get_screenshot_as_file("./image/error.png")
            raise 
