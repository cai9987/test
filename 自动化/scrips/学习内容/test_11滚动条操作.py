from selenium import webdriver

from time import sleep

driver = webdriver.Firefox()

driver.implicitly_wait(30)

driver.maximize_window()

url = "http://47.107.116.139/phpwind/index.php?m=bbs"

driver.get(url)

# 设置js控制语句
js = "window.scrollTo(0,10000)"

# 执行js语句方法
driver.execute_script(js)

sleep(2)

driver.close()
