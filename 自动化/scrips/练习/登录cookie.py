from selenium import webdriver
import requests
import time

driver = webdriver.Firefox()

url = 'http://127.0.0.1/zentao/user-login.html'
driver.get(url)
# 先登录
driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_id("keepLoginon").click()  # 勾选保持登录
driver.find_element_by_id("submit").click()

time.sleep(3)
allcookies = driver.get_cookies()  # 获取浏览器cookies
print("获取到登录后的cookies:%s" % allcookies)

# 把抓取的cookies添加到s中
s = requests.session()


def add_cookies(allcook):
    """往session添加cookies"""
    try:
        # 添加cookies到CookieJar
        c = requests.cookies.RequestsCookieJar()
        for i in allcook:
            c.set(i["name"], i['value'])

        s.cookies.update(c)  # 更新session里cookies
    except Exception as msg:
        print(u"添加cookies的时候报错了：%s" % str(msg))


# 调用添加cookies函数
add_cookies(allcookies)

print("打印s里面是否添加成功了")
print(s.cookies)
# 访问一个登录之后的页面,看是不是能访问了
r1 = s.get("http://127.0.0.1/zentao/my/")
print(r1.content.decode("utf-8"))
