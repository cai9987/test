from time import sleep

from selenium import webdriver

import requests


# class User:
def user_login():
    u = "http://test.zaitakugeek.cn:8000/user/email_login"
    header = {
        "Content-Type": "application/json",
    }
    data = {
        "account": "15018248542@163.com",
        "password": "123456"
    }
    tk = requests.post(url=u, json=data, headers=header)

    session = tk.json()['token']
    return session


url = "http://test.zaitakugeek.cn:8080/home/index"
driver = webdriver.Chrome()
driver.maximize_window()
cookies = user_login()
driver.add_cookie({"name":"token","value":cookies})
sleep(5)
driver.refresh()
sleep(5)
driver.close()
