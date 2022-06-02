from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

wait = WebDriverWait(driver,20)

setting_loc = (By.ID,'s-usersetting-top')
wait.until(EC.visibility_of_element_located(setting_loc))
ele = driver.find_element(*setting_loc)

# 启动鼠标操作
ac = ActionChains(driver)
ac.move_to_element(ele)  # 鼠标移动到设置元素上
# 执行鼠标操作
ac.perform()

search_loc = (By.XPATH,'//a[text()="高级搜索"]')
wait.until(EC.visibility_of_element_located(search_loc))
driver.find_element(*search_loc).click()   # 点击高级搜索按钮