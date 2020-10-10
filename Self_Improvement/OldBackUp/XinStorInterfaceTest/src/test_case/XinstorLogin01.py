# -*- coding: utf-8 -*-
import unittest
import xinstorlib
'''
登录
'''
class XinstorLogin01(unittest.TestCase):
    def setUp(self):
        pass

    def testStep(self):
        mylog = xinstorlib.xinstorlogin()
        self.assertEqual(201, mylog.status_code, msg='Login Failed')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

