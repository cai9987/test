from selenium import webdriver

from time import sleep

from selenium.webdriver.support.select import Select

url = "http://test.zaitakugeek.cn:8080/home/index"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

driver.add_cookie({"name": "token", "value": "82f8ca6b6bb4ad1483bbab9e184bfa17f0a5a0c6"})

sleep(2)

driver.refresh()

sleep(30)

# driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div[2]/ul/li[2]/span/span/div").click()
# driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/ul/li[1]/div/div/div[1]/div[1]/span[1]").click()
# driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/div/div/div/div[2]/div/button").click()
# driver.find_element_by_xpath("//*[@id='app']/div[2]/div[4]/div/div/div[2]/form/div[1]/div/div/input").send_keys("我试试")
# driver.find_element_by_xpath("//*[@id='app']/div[2]/div[4]/div/div/div[2]/form/div[2]/div/div/input").send_keys("123")
# driver.find_element_by_xpath("//*[@id='app']/div[2]/div[4]/div/div/div[2]/form/div[3]/div/div/input").send_keys("123")

driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/div[2]/div/div/button[1]").click()
driver.find_element_by_xpath("//*[@id='app']/div[2]/div[3]/div/div/div[2]/form/div[1]/div/div/input").send_keys("自动胡测试")

ul = driver.find_element_by_xpath(
    "//*[@id='app']/div[2]/div[1]/div[2]/div[1]/div/div/div[2]/form/div[2]/div[1]/div/input")
ul.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[1]/span").click()

# driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div[2]/ul/li[5]").click()
# driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div[2]/ul/li[5]").click()
# driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div[2]/ul/li[5]").click()


sleep(3)

driver.close()
