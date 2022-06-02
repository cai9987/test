from selenium import webdriver

from time import sleep

from selenium.webdriver.support.select import Select

url = "http://test.zaitakugeek.cn:8080/home/index"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

driver.add_cookie({"name":"token","value":"82f8ca6b6bb4ad1483bbab9e184bfa17f0a5a0c6"})

sleep(2)

driver.refresh()

sleep(30)
driver.close()
