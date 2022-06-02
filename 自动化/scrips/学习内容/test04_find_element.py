from selenium import webdriver

from time import sleep

from selenium.webdriver.common.by import By

url = "http://47.107.116.139/phpwind/index.php?m=profile"
driver = webdriver.Firefox()
driver.get(url)

driver.find_element(By.NAME, "username").send_keys("admin")

sleep(3)

driver.quit()
