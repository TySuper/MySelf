# -*- coding:utf-8 -*-
from Common.configHttp import RunMain
import json
import faker
import requests
import urllib3
import random
import string

'''去除安全警告，减少日志量'''
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
f = faker.Faker('zh-cn')


class Interface():
    """接口"""

    @staticmethod
    def login():
        loginheaders = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Authorization': 'null',
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'Host': "192.168.170.150:18888",
            'Origin': "https://192.168.170.150:18888",
            'Referer': "https://192.168.170.150:18888"
        }
        loginbody = {
            'username': "yt",
            'password': "Xit12345678"
        }
        loginurl = "https://192.168.170.150:18888" + '/api/auth/'
        testlogin = requests.post(loginurl, data=loginbody, json=loginheaders, verify=False)
        print(testlogin.json())
        if (testlogin.status_code != 201):
            assert (False), "Login Failed"
        return testlogin

    @staticmethod
    def createuser(myauth, myxspdc, account, name, role, phone, email):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'Host': "192.168.170.120:18888",
            'Origin': "https://192.168.170.120:18888",
            'Referer': "https://192.168.170.120:18888",
            'Authorization': myauth,
            'xspdc': myxspdc
        }
        parameters = {
            "username": account,
            "name": name,
            "role": role,
            "phone": phone,
            "email": email
        }
        poolurl = "https://192.168.170.120:18888" + '/api/operator'
        testcreate = requests.post(poolurl, json=parameters, headers=headers, verify=False)
        return testcreate

    @staticmethod
    def updateuser(myauth, myxspdc, name, role, phone, email):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'Host': "192.168.170.120:18888",
            'Origin': "https://192.168.170.120:18888",
            'Referer': "https://192.168.170.120:18888",
            'Authorization': myauth,
            'xspdc': myxspdc
        }
        parameters = {
            "name": name,
            "role": role,
            "phone": phone,
            "email": email
        }
        poolurl = "https://192.168.170.120:18888" + '/api/operator/' + "yt_123"
        testcreate = requests.put(poolurl, json=parameters, headers=headers, verify=False)
        return testcreate

    @staticmethod
    def deleteuser(myauth, myxspdc, account, name, role, phone, email):
        """删除用户"""
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'Host': "192.168.170.120:18888",
            'Origin': "https://192.168.170.120:18888",
            'Referer': "https://192.168.170.120:18888",
            'Authorization': myauth,
            'xspdc': myxspdc
        }
        parameters = {
            "username": account,
            "name": name,
            "role": role,
            "phone": phone,
            "email": email
        }
        poolurl = "https://192.168.170.120:18888/api/operator/" + account
        testcreate = requests.delete(poolurl, json=parameters, headers=headers, verify=False)
        return testcreate

    @staticmethod
    def resetpassword(myauth, myxspdc):
        """重置密码"""
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'Host': "192.168.170.120:18888",
            'Origin': "https://192.168.170.120:18888",
            'Referer': "https://192.168.170.120:18888",
            'Authorization': myauth,
            'xspdc': myxspdc
        }
        # parameters = {
        #     "username": account,
        #     "name": name,
        #     "role": role,
        #     "phone": phone,
        #     "email": email
        # }
        poolurl = "https://192.168.170.120:18888/api/operator/password/" + "gsgdd"
        testcreate = requests.put(poolurl, headers=headers, verify=False)
        return testcreate

    @staticmethod
    def addmorelun(myauth, myxspdc, poolName, lunName):
        """批量增加卷"""
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'Host': "192.168.170.120:18888",
            'Origin': "https://192.168.170.120:18888",
            'Referer': "https://192.168.170.120:18888",
            'Authorization': myauth,
            'xspdc': myxspdc
        }
        parameters = {"pool": poolName,
                      "image": lunName,
                      "size": 1073741824,
                      "cipher_block_size": 4096,
                      "cipher_key_count": 4,
                      "cipher_type": "2",
                      "max_bytes": {},
                      "need_encrypt": "0"}
        poolurl = "https://192.168.170.120:18888/api/iscsi/disk"
        testcreate = requests.post(poolurl, json=parameters, headers=headers, verify=False)
        return testcreate

    @staticmethod
    def addrescovery(myauth, myxspdc):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'Host': "192.168.170.120:18888",
            'Origin': "https://192.168.170.120:18888",
            'Referer': "https://192.168.170.120:18888",
            'Authorization': myauth,
            'xspdc': myxspdc
        }
        parameters = {
            "bak_snap_id": 51,
            "src_pool": "yt_pool",
            "src_image": "jsm_lun"
        }
        poolurl = "https://192.168.170.120:18888/api/image_bak/rollback"
        testcreate = requests.post(poolurl, json=parameters, headers=headers, verify=False)
        return testcreate

    @staticmethod
    def deletebackup(myauth, myxspdc,j):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'Host': "192.168.170.150:18888",
            'Origin': "https://192.168.170.150:18888",
            'Referer': "https://192.168.170.150:18888",
            'Authorization': myauth,
            'xspdc': myxspdc
        }
        parameters = {
            "bak_id": j,
            "force_del": 0,
            "bak_image_save": 0,
            "bak_snap_save": "", "del_bak_snaps": ""}

        poolurl = "https://192.168.170.150:18888/api/image_bak/bak_config/del_bak_config"
        testcreate = requests.post(poolurl, json=parameters, headers=headers, verify=False)
        return testcreate

    @staticmethod
    def deletelun(myauth, myxspdc,j):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Accept': 'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'Host': "192.168.170.150:18888",
            'Origin': "https://192.168.170.150:18888",
            'Referer': "https://192.168.170.150:18888",
            'Authorization': myauth,
            'xspdc': myxspdc
        }
        parameters = {
            "bak_id": j,
            "force_del": 0,
            "bak_image_save": 0,
            "bak_snap_save": "", "del_bak_snaps": ""}
        poolurl = "https://192.168.225.132:18888/api/iscsi/disk/GLOpool/FCpycs"
        testcreate = requests.delete(poolurl, json=parameters, headers=headers, verify=False)
        return testcreate