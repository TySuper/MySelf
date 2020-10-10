# -*- coding: utf-8 -*-
import unittest
import xinstorlib
from selenium import webdriver
'''
登录
'''
class XinstorLogin01(unittest.TestCase):
    def setUp(self):
        pass

    def testStep(self):
        browser = webdriver.Chrome()
        browser.get("https://192.168.225.133:18888")


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

