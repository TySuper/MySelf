# -*- coding: utf-8 -*-
import unittest
import xinstorlib
import random
import common
import string
'''
获取pool相关信息
'''
class GetPool01(unittest.TestCase):
    def setUp(self):
        mylog = xinstorlib.xinstorlogin()
        self.xp = mylog.json().get('data').get('xspdc')
        self.auth = mylog.headers['Authorization']

    def testStep(self):
        myget = xinstorlib.getpool(myauth=self.auth, myxspdc=self.xp)
        self.assertEqual(200, myget.status_code, msg='Get Pool Failed')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
