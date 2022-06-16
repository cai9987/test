from selenium.webdriver.common.by import By

url = "http://test.zaitakugeek.cn:8080/login"

login_link = By.CSS_SELECTOR,'.el-button--mini > span'
login_input_username = By.XPATH,'html/body/div[1]/div/div[2]/div/form/div/div[1]/div/div/div[1]/input'
login_input_password = By.XPATH,'html/body/div[1]/div/div[2]/div/form/div/div[2]/div/div/div[1]/input'
login_btn = By.CSS_SELECTOR,'.el-button.el-button--primary'

login_up_err_text = By.XPATH,'/html/body/div[2]/p'
login_err_username_text = By.XPATH,'/html/body/div/div/div[2]/div/form/div/div[1]/div/div/div[2]'
login_err_password_text = By.XPATH,'/html/body/div/div/div[2]/div/form/div/div[2]/div/div/div[2]'

login_if_success = By.XPATH,'/html/body/div/div/div/div[1]/div/div[2]/div/span'
login_quit = By.XPATH,'/html/body/ul/li[4]'
login_quit_btn = By.XPATH,'/html/body/div[2]/div/div[3]/button[2]/span'

