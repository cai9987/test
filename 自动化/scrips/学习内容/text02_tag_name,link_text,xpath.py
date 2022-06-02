from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

url = "http://47.107.116.139/phpwind/index.php?m=u&c=login"
driver.get(url)
# 用元素标签名称定位方法，标签名（查看元素时尖括号），tag_name
# driver.find_element_by_tag_name("input").send_keys("15018248542")

# 用xpath定位，用相对路径和绝对路径查找元素
driver.find_element_by_xpath(".//*[@id='J_u_login_username']").send_keys("jiasuo")
driver.find_element_by_xpath(".//*[@id='J_u_login_password']").send_keys("123456")
driver.find_element_by_xpath("html/body/div[1]/div[2]/div/div[1]/div/form/div/dl[4]/dd/button").click()

# 用link_text定位，点击链接地址
# driver.find_element_by_link_text("登录").click()

# 用partial_link_text定位，点击链接地址，模糊匹配
# driver.find_element_by_partial_link_text("登").click()


sleep(5)

driver.quit()
