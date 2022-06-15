from selenium.webdriver.common.by import By

url = 'http://test.zaitakugeek.cn:8080/enterpriseCenter/info'

token = {"name": "token", "value": "c1b1e9dab44a53eb1f81337a7fa8ff7603a621f7"}

task_btn = By.XPATH, '//*[@id="webApp"]/div/div[2]/div[1]/ul/button/span'
task_title = By.XPATH, "//*[@id='webApp']/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div/div[1]/input"
task_date_click = By.XPATH, "/html/body/div/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[3]/div/div/input"
task_date = By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[5]/div/span"
task_money_min = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[4]/div[1]/div/div/div/input"
task_money_max = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[4]/div[2]/div/div/div/input"
task_want_day = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[5]/div/div/input"
task_people_sum = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[6]/div/div/input"
task_describe = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[3]/div[2]/div[1]/div/div/textarea"
task_save_btn = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/button"

task_titLe_err_text = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div/div[2]"
task_field_err_text = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div[2]"
