from selenium import webdriver

from time import sleep

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()

url = "http://47.107.116.139/phpwind/index.php?c=thread&fid=2"

driver.get(url)

driver.maximize_window()
# 隐式等待
driver.implicitly_wait(10)
# 下拉选择框
# 通过索引定位
# Select(driver.find_element_by_css_selector(".J_sidebar_forum_toggle>a")).select_by_index(1)
# 通过value值定位
# Select(driver.find_element_by_css_selector(".J_sidebar_forum_toggle>a")).select_by_value("xbk")
# 通过文本内容定位
# Select(driver.find_element_by_css_selector(".J_sidebar_forum_toggle>a")).select_by_visible_text("新板块")

sleep(2)

driver.close()
