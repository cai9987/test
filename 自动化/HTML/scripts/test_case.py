# import unittest
# from HTML.tools.HTMLTestRunner import HTMLTestRunner
#
# # 实例化loader方法，多个文件的用例一起执行
# # loader = unittest.TestLoader().discover("../case")
# # 只运行某个文件
# loader = unittest.TestLoader().discover("./", pattern="test01.py")
# # 运行测试用例
# with open("../report/report.html", "wb") as f:
#     HTMLTestRunner(stream=f).run(loader)
