# -*- coding: utf-8 -*-
import unittest
import xinstorlib
import random
import common
import string

'''
创建卷
'''
class CreateVolume01(unittest.TestCase):
    def setUp(self):
        mylog = xinstorlib.xinstorlogin()
        self.xp = mylog.json().get('data').get('xspdc')
        self.auth = mylog.headers['Authorization']
        createpool = xinstorlib.createpool(myauth=self.auth, myxspdc=self.xp, poolname=common.poolname,
                                         groupname=common.groupname, maxbytes=1048576)
        self.assertEqual(201, createpool.status_code, msg='Create Pool Failed')

    def testStep(self):
        testname = 'ZHL-Test-' + ''.join(random.sample(string.ascii_letters + string.digits, 3))
        createvolume = xinstorlib.createvolume(myauth=self.auth, myxspdc=self.xp, poolname=common.poolname,
                                           volumename=testname, size=1048576)
        self.assertEqual(201, createvolume.status_code, msg='Create Volume Failed')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
