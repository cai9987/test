from selenium.webdriver.common.by import By

url = "http://test.zaitakugeek.cn:8080/task/details?id=1322804527334432"

token = {"name": "token", "value": "9bfcbc362357b66c97dde24d04bc33b2da89a827"}

task_sign = By.XPATH, '/html/body/div/div/div/div[3]/div/div/div[1]/div/div[1]/div[2]/div[3]/button/span'
task_want_time = By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div[2]/form[1]/div/div[1]/div/div/div/input'
task_want_money = By.XPATH, '//*[@id="webApp"]/div/div[3]/div/div/div[1]/div/div[2]/div/div[2]/form[1]/div/div[2]/div/div/div/input'
task_dir = By.XPATH, "//*[@id='webApp']/div/div[3]/div/div/div[1]/div/div[2]/div/div[2]/form[1]/div/div[3]/div/div/div/textarea"
task_ok_btn = By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div[2]/form[1]/div/div[3]/div/div/div/textarea"

# 错误文本
time_err_text = By.XPATH, '//*[@id="webApp"]/div/div[3]/div/div/div[1]/div/div[2]/div/div[2]/form[1]/div/div[1]/div/div/div[2]'
money_err_text = By.XPATH, '//*[@id="webApp"]/div/div[3]/div/div/div[1]/div/div[2]/div/div[2]/form[1]/div/div[2]/div/div/div[2]'
