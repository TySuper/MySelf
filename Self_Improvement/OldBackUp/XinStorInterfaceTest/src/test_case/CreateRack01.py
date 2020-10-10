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
        for i in range(1,1000,1):
            time.sleep(1)
            testname = '-_-Rack-_-' + str(i)
            mycreate = xinstorlib.createrack(myauth=auth, myxspdc=xp, rackname=testname)
            self.assertEqual(201, mycreate.status_code, msg='Create User Failed')
            print testname + 'create success'

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
