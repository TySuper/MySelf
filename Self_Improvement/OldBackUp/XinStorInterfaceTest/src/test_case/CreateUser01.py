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
        testname = 'zhenghongli_' + ''.join(random.sample(string.lowercase + string.digits, 3))
        mycreate = xinstorlib.createuser(myauth=auth, myxspdc=xp, account=testname, name='zhenghongli', role='system',
                                         phone='13688160168', email='zhenghongli@xitcorp.com')
        self.assertEqual(201, mycreate.status_code, msg='Create User Failed')
        print mycreate.json()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
