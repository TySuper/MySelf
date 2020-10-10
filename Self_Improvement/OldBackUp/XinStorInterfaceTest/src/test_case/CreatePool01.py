# -*- coding: utf-8 -*-
import unittest
import xinstorlib
import random
import common
import string

class CreatePool01(unittest.TestCase):
    def setUp(self):
        pass

    def testStep(self):
        mylog = xinstorlib.xinstorlogin()
        xp = mylog.json().get('data').get('xspdc')
        auth = mylog.headers['Authorization']
        testname = 'ZHL-Test-' + ''.join(random.sample(string.ascii_letters + string.digits, 3))
        mycreate = xinstorlib.createpool(myauth=auth, myxspdc=xp, poolname=testname, groupname='zhl',
                                           maxbytes=1048576)
        self.assertEqual(201, mycreate.status_code, msg='Create Pool Failed')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
