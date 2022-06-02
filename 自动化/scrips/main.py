from selenium import webdriver  # 导入webdriver

from time import sleep

driver = webdriver.Chrome()  # 获取谷歌浏览器对象
# 打开地址
driver.get("http://test.zaitakugeek.cn:8080/recommend/index")
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()

# id(使用元素的class属性定位)
# name(使用元素的class属性定位)
# class_name(使用元素的class属性定位)
# teg_name(标签名称<标签名...>)
# link_text(定位超连接a标签)
# partial_link_text(定位超链接a标签 模糊)
# xpath(基于元素路径)
# css(元素选择器)
