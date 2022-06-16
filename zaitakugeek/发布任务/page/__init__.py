from selenium.webdriver.common.by import By

url = 'http://test.zaitakugeek.cn:8080/enterpriseCenter/info'

token = {"name": "token", "value": "c1b1e9dab44a53eb1f81337a7fa8ff7603a621f7"}

# 发布任务按钮
task_btn = By.XPATH, '//*[@id="webApp"]/div/div[2]/div[1]/ul/button/span'
# 需求标题
task_title = By.XPATH, "//*[@id='webApp']/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div/div[1]/input"
# 所属领域
task_field_click = By.XPATH, "//*[@id='webApp']/div/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div/div/input"
task_field_one = By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/ul/li[4]/span"
task_field_two = By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[5]/span"
# 报名截止
task_date_click = By.XPATH, "/html/body/div/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[3]/div/div/input"
task_date = By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[5]/div/span"
# 预算
task_money_min = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[4]/div[1]/div/div/div/input"
task_money_max = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[4]/div[2]/div/div/div/input"
# 预计天数
task_want_day = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[5]/div/div/input"
# 招募人数
task_people_sum = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[6]/div/div/input"
# 描述
task_describe = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[3]/div[2]/div[1]/div/div/textarea"
# 保存按钮
task_save_btn = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/button"


# 错误提示信息
task_titLe_err_text = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[1]/div/div[2]"
task_field_err_text = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div[2]"
task_min_money_err_text = By.XPATH, "//*[@id='webApp']/div/div[2]/div/div/form/div[1]/div[2]/div/div[4]/div[1]/div/div/div[2]"
task_max_money_err_text = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[4]/div[2]/div/div/div[2]"
task_want_day_err_text = By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/form/div[1]/div[2]/div/div[5]/div/div[2]"
task_people_sum_err_text = By.XPATH, "//*[@id='webApp']/div/div[2]/div/div/form/div[1]/div[2]/div/div[6]/div/div[2]"
task_describe_err_text = By.XPATH, "//*[@id='webApp']/div/div[2]/div/div/form/div[3]/div[2]/div[1]/div/div[2]"
