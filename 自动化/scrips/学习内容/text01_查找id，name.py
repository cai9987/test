from time import sleep

from selenium import webdriver

#
# driver = webdriver.Firefox()
#
# url = "http://47.107.116.139/phpwind/index.php?m=u&c=login"
# driver.get(url)

# 用name查找
# username = driver.find_element_by_name("username")
# password = driver.find_element_by_name("password")

# 用id查找
# username = driver.find_element_by_id("J_u_login_username")
# password = driver.find_element_by_id("J_u_login_password")


# username.send_keys("jiasuo")
# password.send_keys("123456")
# driver.find_element_by_xpath(".//*[@id='J_u_login_form']/div/dl[4]/dd/button").click

# sleep(3)
#
# driver.quit()


driver = webdriver.Chrome()

url = "http://test.zaitakugeek.cn:8080/login"
driver.get(url)

driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/form/div/div[1]/div/div/input").send_keys("15018248542")
driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/form/div/div[2]/div/div/input").send_keys("123456")

sleep(3)
driver.quit()
