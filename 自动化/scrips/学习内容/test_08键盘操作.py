from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# 隐式等待
driver.implicitly_wait(10)

url = "https://www.zaitakugeek.cn/login"
driver.get(url)


username = driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/form/div/div[1]/div/div/input")
driver.maximize_window()
# 输入用户名
username.send_keys("150182485422")
sleep(2)
# 删除
username.send_keys(Keys.BACK_SPACE)
sleep(2)
# 全选用户名
username.send_keys(Keys.CONTROL,"a")
sleep(2)
# 复制
username.send_keys(Keys.CONTROL,"c")
sleep(2)
# 粘贴
password = driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/form/div/div[2]/div/div/input")
password.send_keys(Keys.CONTROL,"v")

sleep(2)

driver.close()
