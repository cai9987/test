import unittest
# 实例化loader方法，多个文件的用例一起执行
# loader = unittest.TestLoader().discover("../case")
# 只运行某个文件
loader = unittest.TestLoader().discover("./report",pattern="*01.py")
# 运行测试用例
unittest.TextTestRunner().run(loader)

