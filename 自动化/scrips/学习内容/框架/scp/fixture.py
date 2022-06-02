import unittest


class Test(unittest.TestCase):
    # 首先执行
    @classmethod
    def setUpClass(cls):
        print("123")

    # 最后执行
    @classmethod
    def tearDownClass(cls):
        print("234")

    def setUp(self):
        print("执行")

    def tearDown(self):
        print("执行完")

    def test01(self):
        print("执行1")

    def test02(self):
        print("执行2")
