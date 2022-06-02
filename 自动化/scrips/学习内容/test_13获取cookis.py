from selenium import webdriver

from time import sleep

driver = webdriver.Chrome()

driver.maximize_window()

url = "http://test.zaitakugeek.cn:8080/home/index"
# url = "https://www.baidu.com"
driver.get(url)

# driver.add_cookie({"name":"BDUSS","value":"nU3NnZhcDRXZWtlanNob29Odng4bU04VTdiVWJ0Q3hIWXUzdjNXQWdvdkM0ejVpSUFBQUFBJCQAAAAAAAAAAAEAAAALvMVyu~DIy8qkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMJWF2LCVhdiR"})


driver.add_cookie({
    'domain': '.test.zaitakugeek.cn',
    'httpOnly': False,
    'path': '/',
    'secure': False,
    'name': 'csrftoken',
    'value': "hISPVXWQSYKhZ2Bt1YrbJ8V5z1C5khwBpKg17pEv3CFb2XG3KJJiNQjGLHiaeJJZ"
})

cookies = driver.get_cookies()
print(cookies)
for co in cookies:
    print(co)
sleep(2)

driver.refresh()

sleep(2)

driver.close()
