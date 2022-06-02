from selenium import webdriver

from time import sleep

url = "http://47.107.116.139/phpwind/index.php?m=profile"
driver = webdriver.Firefox()
driver.get(url)

driver.find_element_by_css_selector("#J_u_login_username").send_keys('jiasuo')
# driver.find_element_by_css_selector("#J_u_login_password").send_keys("123456")
driver.find_element_by_css_selector("[name='password']").send_keys("123456")
# driver.find_element_by_css_selector("#J_bbs_sign").send_keys("我命由我不由天")

sleep(5)

driver.quit()
