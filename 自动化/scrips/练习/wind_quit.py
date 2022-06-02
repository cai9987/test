from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

url = "http://47.107.116.139/phpwind/"
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url)
driver.find_element_by_id("J_sidebar_login").click()
driver.find_element_by_id("J_u_login_username").send_keys("jiasuo")
driver.find_element_by_id("J_u_login_password").send_keys("123456")
driver.find_element_by_css_selector(".btn.btn_big.btn_submit.mr20").click()
sleep(2)


driver.find_element_by_css_selector("#J_head_user_a").click()


sleep(2)
driver.find_element_by_xpath("html/body/div[1]/header/div/div[5]/div/div/div/ul[2]/li[2]/a").click()
sleep(2)
driver.close()



