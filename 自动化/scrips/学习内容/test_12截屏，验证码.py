from selenium import webdriver

from time import sleep

driver = webdriver.Firefox()

driver.implicitly_wait(30)

driver.maximize_window()

url = "http://47.107.116.139/phpwind/index.php?m=u&c=login"

driver.get(url)

driver.find_element_by_css_selector("#J_u_login_username").send_keys("jiasuo")
driver.find_element_by_css_selector("#J_u_login_password").send_keys("123456")
# 截图
# driver.get_screenshot_as_file("../admin.png")

# cookis操作

sleep(2)

driver.close()
