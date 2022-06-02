from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()

url = "http://47.107.116.139/phpwind/index.php?m=u&c=login"
driver.get(url)

# 获取用户名文本框大小.size
var = driver.find_element_by_xpath(".//*[@id='J_u_login_username']").size
print("用户名文本框大小为：", var)
# 获取页面上第一个超文本链接内容.text
text = driver.find_element_by_xpath("html/body/div[1]/header/div/nav/div/ul/li[1]/a").text
print("页面上第一个超文本链接内容为：", text)
# 获取页面上第一个超文本链接地址.get_attribute()
att = driver.find_element_by_xpath("html/body/div[1]/header/div/nav/div/ul/li[1]/a").get_attribute("href")
print("页面上第一个超文本链接地址为：", att)
# 判断span元素是否可用.is_displayed()
dis = driver.find_element_by_css_selector("span").is_displayed()
print("判断span元素是否可用:", dis)
# 无效按钮.is_enabled()
enabled = driver.find_element_by_css_selector(".btn.btn_big.btn_submit.mr20").is_enabled()
print("无效按钮:", enabled)
# 判断选择信息.is_selected()
selected = driver.find_element_by_css_selector(".cc.pick>dd").is_selected()
print("选择自动登录：", selected)

sleep(2)
driver.quit()