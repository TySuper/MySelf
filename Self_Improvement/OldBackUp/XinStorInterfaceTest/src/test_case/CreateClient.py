# -*- coding: utf-8 -*-
import unittest
import xinstorlib
import random
import common
import string

class CreateUser01(unittest.TestCase):
    def setUp(self):
        pass

    def testStep(self):
        mylog = xinstorlib.xinstorlogin()
        xp = mylog.json().get('data').get('xspdc')
        auth = mylog.headers['Authorization']
        testiqn = "iqn.2020-03.com.zhenghongli:" + ''.join(random.sample(string.lowercase + string.digits, 3))
        mycreate = xinstorlib.creatclient(myauth=auth, myxspdc=xp, target_iqn=common.target_iqn, client_iqn=testiqn)
        self.assertEqual(201, mycreate.status_code, msg='Create Client Failed')
        print (mycreate.json())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
