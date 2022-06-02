from selenium import webdriver

from time import sleep

from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
url = "http://test.zaitakugeek.cn:8080/login"
driver.get(url)

action = ActionChains(driver)
# 定位用户名，在用户名上右击鼠标 预期：粘贴
# action.context_click(
#     driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/form/div/div[5]/a[1]")).perform()
# sleep(2)
# 发送密码双击，预期：选中密码
# driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/form/div/div[2]/div/div/input").send_keys('123456')
action.double_click(driver.find_element_by_xpath
                    ("//*[@id='app']/div[2]/div[2]/form/div/div[2]/div/div/input").send_keys('123456')).perform()
sleep(2)
# 移动到忘记密码，预期：变红
action.move_to_element(driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/form/div/div[3]/a")).perform()
sleep(2)
driver.quit()
