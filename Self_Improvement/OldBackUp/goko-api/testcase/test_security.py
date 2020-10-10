# -*- coding:utf-8 -*-
from interface.interface import Interface
import unittest
from Common.getKeyword import get_result_for_keyword, get_results_for_label_keyword, get_results_for_keyword
import time
import requests
import json
import faker
import random
f =faker.Faker("ZH-CN")

s = requests.session()
now = time.strftime("%Y-%m-%d %H:%M:%S")


class TestMain(unittest.TestCase):

    def setUp(self):
        print("测试开始")
        self.mylog = Interface().login()
        response = self.mylog.json()
        # print(json.dumps(response, ensure_ascii=False, indent=2))
        self.authorization = self.mylog.headers['Authorization']

    def test_01_createuser(self):
        xp = self.mylog.json().get('data').get('xspdc')
        auth = self.authorization
        testname = "".join(random.sample("abcdefgedfghxvcvsdasdasdasdsdasdas",5))
        name = f.name()
        phone = f.phone_number()
        email = f.email()
        userInfo = [testname,name,phone,email]
        print(testname,name,phone,email)
        mycreate = Interface().createuser(myauth=auth, myxspdc=xp, account=testname, name=name, role='system',
                                          phone=phone, email=email)
        response = mycreate.json()
        res = json.dumps(response, ensure_ascii=False, indent=2)
        print(res)
        return userInfo

    def test_02_update(self):
        xp = self.mylog.json().get('data').get('xspdc')
        auth = self.authorization
        mycreate = Interface().updateuser(myauth=auth, myxspdc=xp, name='test', role='system',
                                          phone='13688160165', email='test123@xitcorp.com')
        response = mycreate.json()
        res = json.dumps(response, ensure_ascii=False, indent=2)
        print(res)

    def test_03_delete(self):
        userInfo = self.test_01_createuser()
        xp = self.mylog.json().get('data').get('xspdc')
        auth = self.authorization
        mycreate = Interface().deleteuser(myauth=auth, myxspdc=xp, account=userInfo[0], name=userInfo[1], role='system',
                                          phone=userInfo[2], email=userInfo[3])
        response = mycreate.json()
        res = json.dumps(response, ensure_ascii=False, indent=2)
        print(res)

    def test_04_reset(self):
        """重置密码"""
        xp = self.mylog.json().get('data').get('xspdc')
        auth = self.authorization
        mycreate = Interface().resetpassword(myauth=auth, myxspdc=xp)
        response = mycreate.json()
        res = json.dumps(response, ensure_ascii=False, indent=2)
        print(res)

if __name__ == '__main__':
    unittest.main()
