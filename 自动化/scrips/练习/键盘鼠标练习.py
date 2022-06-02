from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()

url ="http://47.107.116.139/phpwind/index.php?m=u&c=login"

driver.get(url)

driver.maximize_window()


username = WebDriverWait(driver,timeout=10,poll_frequency=0.5).until(lambda x:x.find_element_by_css_selector("#J_u_login_username"))
username.send_keys("jiasuo1")
sleep(2)
# 键盘操作删除
username.send_keys(Keys.BACK_SPACE)
# 鼠标操作,双击
action = ActionChains(driver)
action.double_click(driver.find_element_by_css_selector("#J_u_login_username")).perform()
sleep(2)
# 键盘复制
username.send_keys(Keys.CONTROL,"c")
sleep(2)
# 键盘粘贴
password = WebDriverWait(driver,timeout=10,poll_frequency=0.5).until(lambda x:x.find_element_by_css_selector("#J_u_login_password"))
password.send_keys(Keys.CONTROL,"v")
sleep(2)

action.move_to_element(driver.find_element_by_css_selector("#footer_segment>p>a")).perform()

sleep(2)

driver.close()