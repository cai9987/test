# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://mail.163.com/")

driver.find_element_by_name("email").send_keys("15018248542")
driver.find_element_by_name("password").send_keys("cjswan1314++")

driver.find_element_by_css_selector("#dologin").click()

time.sleep(10)

driver.quit()
