from selenium.webdriver.common.by import By

url = "http://test.zaitakugeek.cn:8080/enterpriseCenter/changePass"

token = {"name": "token", "value": "c1b1e9dab44a53eb1f81337a7fa8ff7603a621f7"}

input_old_password = By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/input'
input_new_password = By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div/form/div[2]/div/div[1]/input'
again_input_new_password = By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div/form/div[3]/div/div[1]/input'
password_btn = By.XPATH,"//*[@id='webApp']/div/div[2]/div[2]/div/form/div[5]/div/button[2]"
password_clear =By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/form/div[5]/div/button[1]/span"

# 错误文本
input_new_password_err_text = By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div/form/div[2]/div/div[2]'
again_input_new_password_err_text = By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div/form/div[3]/div/div[2]'
up_err_text = By.XPATH,'/html/body/div[2]/p'

