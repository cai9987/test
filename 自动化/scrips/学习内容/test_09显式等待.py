from selenium import webdriver
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

url = "https://www.zaitakugeek.cn/login"
driver.get(url)

el = WebDriverWait(driver, timeout=30, poll_frequency=0.5).until \
    (lambda x: x.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/form/div/div[1]/div/div/input"))
# 代码运行起来，el才是元素
el.send_keys("15018248542")
sleep(2)

driver.close()
