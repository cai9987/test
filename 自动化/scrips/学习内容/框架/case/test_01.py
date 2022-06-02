# 导包
import unittest


def add(x, y):
    return x + y


# 新建测试类，进行继承
class TestCase(unittest.TestCase):
    # 测试方法以test开头
    def test_add(self):
        result = add(1,1)
        print("结果为:",result)

    def test_add02(self):
        result = add(2,1)
        print("结果为:",result)
