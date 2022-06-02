from selenium import webdriver

from time import sleep

driver = webdriver.Chrome()

driver.maximize_window()

url = "http://test.zaitakugeek.cn:8080/home/index"
# url = "https://www.baidu.com"
# url = "http://47.107.116.139/phpwind/index.php?m=u&c=login"
driver.get(url)
# driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div[2]/ul/li[3]/div[1]").click()

print(driver.get_cookies())
# driver.add_cookie({"name": "BDUSS","value": "nU3NnZhcDRXZWtlanNob29Odng4bU04VTdiVWJ0Q3hIWXUzdjNXQWdvdkM0ejVpSUFBQUFBJCQAAAAAAAAAAAEAAAALvMVyu~DIy8qkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMJWF2LCVhdiR"})
driver.add_cookie({"name":"token","value":"2dfc33e02dec5dfeaccbb309d151197bbaa0157f"})
sleep(2)

# driver.find_element_by_css_selector("#J_u_login_username").send_keys("jiasuo")
# driver.find_element_by_css_selector("#J_u_login_password").send_keys("123456")
# driver.find_element_by_css_selector(".btn.btn_big.btn_submit.mr20").click()

cookies = driver.get_cookies()
print(cookies)
# for co in cookies:
#     print(co['name'])
sleep(2)

driver.refresh()

print(driver.get_cookies())

sleep(2)

driver.close()
