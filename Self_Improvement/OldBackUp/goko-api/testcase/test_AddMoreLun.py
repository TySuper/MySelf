# -*- coding:utf-8 -*-
from interface.interface import Interface
import unittest
from Common.getKeyword import get_result_for_keyword, get_results_for_label_keyword, get_results_for_keyword
import time
import requests
import json
import faker
import random

f = faker.Faker("ZH-CN")

s = requests.session()
now = time.strftime("%Y-%m-%d %H:%M:%S")


class TestMain(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.mylog = Interface().login()
        response = self.mylog.json()
        # print(json.dumps(response, ensure_ascii=False, indent=2))
        self.authorization = self.mylog.headers['Authorization']

    def test_01_addlun(self):
        xp = self.mylog.json().get('data').get('xspdc')
        auth = self.authorization
        for i in range(1, 15):
            poolName = "pool"
            lunName = "".join(
                random.sample("abcdefgedfghxvcvsdasdasdasdsdasdadsdsdsweqwetnghjhguyytuhjhkuioulnbnvxcvxcvzxcxas", 5))
            mycreate = Interface().addmorelun(myauth=auth, myxspdc=xp, poolName=poolName, lunName=lunName)
            response = mycreate.json()
            res = json.dumps(response, ensure_ascii=False, indent=2)
            print(res)

    def test_02_delete(self):
        xp = self.mylog.json().get('data').get('xspdc')
        auth = self.authorization
        for i in range(1, 200):
            mycreate = Interface().deletebackup(myauth=auth, myxspdc=xp,j=i)
            response = mycreate.json()
            res = json.dumps(response, ensure_ascii=False, indent=2)
            print(res)


    def test_03_delete(self):
        """删除lun"""
        xp = self.mylog.json().get('data').get('xspdc')
        auth = self.authorization
        for i in range(1, 200):
            mycreate = Interface().deletebackup(myauth=auth, myxspdc=xp, j=i)
            response = mycreate.json()
            res = json.dumps(response, ensure_ascii=False, indent=2)
            print(res)