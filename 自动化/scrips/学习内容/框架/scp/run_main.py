# 导入需要的包
import unittest
# 导入其他文件
from scrips.学习内容.框架.scp.testcase import TestCase

# 实例化方法
suite = unittest.TestSuite()
# 执行测试方法，一次执行一条
# suite.addTest(TestCase("test_add"))

# 执行测试方法，一次执行一个类的所有用例
suite.addTest(unittest.makeSuite(TestCase))

# 执行测试用例
runner = unittest.TextTestRunner()
runner.run(suite)
