# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://www.zentao.net/ ')

# driver.find_element_by_link_text('登录').click()
# driver.find_element_by_class_name('qq').click()
# driver.switch_to.frame('ptlogin_iframe')                             # 通过frame方式定位
# driver.find_element_by_css_selector('#switcher_plogin').click()
# driver.find_element_by_id('u').send_keys('*******')
# driver.find_element_by_id('p').send_keys('*******')
# driver.find_element_by_id('login_button').click()


driver.find_element_by_link_text('登录').click()
driver.find_element_by_css_selector("#account").send_keys("15018248542@163.com")
driver.find_element_by_css_selector("#password").send_keys("cjswan1314++")
driver.find_element_by_css_selector("#submit").click()
time.sleep(10)

do = driver.get_cookies()
print(do)

driver.quit()
