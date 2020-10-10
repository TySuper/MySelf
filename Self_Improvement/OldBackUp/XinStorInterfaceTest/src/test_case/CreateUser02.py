# -*- coding: utf-8 -*-
import unittest
import xinstorlib
import random
import common
import string
import time

class CreateUser02(unittest.TestCase):
    def setUp(self):
        pass

    def testStep(self):
        mylog = xinstorlib.xinstorlogin()
        xp = mylog.json().get('data').get('xspdc')
        auth = mylog.headers['Authorization']
        for i in range(1,64,1):
            time.sleep(2)
            testname = 'zhenghongli_ad_' + str(i)
            mycreate = xinstorlib.createuser(myauth=auth, myxspdc=xp, account=testname, name='zhenghongli', role='audit',
                                         phone='13688160168', email='zhenghongli@xitcorp.com')
            self.assertEqual(201, mycreate.status_code, msg='Create User Failed')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
