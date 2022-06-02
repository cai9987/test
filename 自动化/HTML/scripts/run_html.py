# 将HTML文件放在指定位置
import time
import unittest

from HTML.tools.HTMLTestRunner import HTMLTestRunner

loader = unittest.defaultTestLoader.discover("./", pattern="test01.py")

report_dir = "../report/test_case.html"

with open(report_dir, "wb") as f:
    HTMLTestRunner(stream=f, verbosity=2, title="xx项目自动化测试报告").run(loader)

# time.strftime("%Y_%m_d_%H_%M_S")
