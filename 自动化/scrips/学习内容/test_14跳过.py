import unittest

var = 30


class Test01(unittest.TestCase):
    # 直接跳过
    # @unittest.skip("未完成")
    def test01(self):
        print("test01")
        """
            功能未完成
        """

    # 满足条件跳过
    @unittest.skipIf(var > 25, "大于25，跳过")
    def test02(self):
        print("test02")
