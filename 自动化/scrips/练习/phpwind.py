import unittest
from time import sleep
from selenium import webdriver

class TestWind(unittest.TestCase):
    def setUp(self) -> None:
        url = "http://47.107.116.139/phpwind/index.php?m=bbs"
        self.driver = webdriver.Firefox()
