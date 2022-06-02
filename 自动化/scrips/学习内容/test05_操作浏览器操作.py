from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()

url = "http://test.zaitakugeek.cn:8080/login"
driver.get(url)
# 将浏览器最大化
driver.maximize_window()
sleep(2)
# 固定浏览器大小
driver.set_window_size(300, 200)
sleep(2)

# 移动浏览器窗口位置
driver.set_window_position(320, 150)
sleep(2)
# 将浏览器最大化
driver.maximize_window()
sleep(2)
# 点击论坛
driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/form/div/div[5]/a[1]").click()
sleep(2)
# 执行后退，回到注册页面
# driver.back()
# sleep(2)
# # 执行前进，前进到到论坛页面
# driver.forward()
# sleep(2)
#
# driver.quit()

# 先输入用户名，为了刷新演示
driver.find_element_by_xpath("//*[@id='app']/div[2]/div[2]/form/div/div[1]/div/div/div[3]/input").send_keys("15018248542")
sleep(2)
# 刷新
driver.refresh()
sleep(2)
# 获取title,不加()
driver.title()
print("当前页面title：", driver.title)
sleep(2)
# 获取当前url,不加()
driver.current_url()
print("获取当前url：", driver.current_url)
# 打开新窗口
# 关闭主窗口
driver.close()
sleep(2)
# 关闭所有窗口
driver.quit()
