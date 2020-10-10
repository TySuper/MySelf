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

    def test_01_addrescovery(self):
        xp = self.mylog.json().get('data').get('xspdc')
        auth = self.authorization
        for i in range(1, 50):
            mycreate = Interface().addrescovery(myauth=auth, myxspdc=xp, )
            response = mycreate.json()
            res = json.dumps(response, ensure_ascii=False, indent=2)
            print(res)


    def test_02_deleterescovery(self):
        """删除备份恢复记录"""