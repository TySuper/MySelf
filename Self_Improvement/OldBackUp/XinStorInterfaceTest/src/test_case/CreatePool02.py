# -*- coding: utf-8 -*-
import unittest
import xinstorlib
import random
import common
import string
import time
'''
循环创建多个存储池
'''

class CreatePool02(unittest.TestCase):
    def setUp(self):
        pass

    def testStep(self):
        mylog = xinstorlib.xinstorlogin()
        xp = mylog.json().get('data').get('xspdc')
        auth = mylog.headers['Authorization']
        for i in range(1, 30, 1):
            print "create:" + str(i)
            time.sleep(2)
            testname = common.poolname + '-' + str(i)
            mycreate = xinstorlib.createpool(myauth=auth, myxspdc=xp, poolname=testname, groupname=common.groupname,
                                               maxbytes=1048576)
            self.assertEqual(201, mycreate.status_code, msg='Create Pool Failed')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
