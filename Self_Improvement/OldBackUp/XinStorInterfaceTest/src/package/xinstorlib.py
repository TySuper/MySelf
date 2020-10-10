#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import common
import urllib3

'''去除安全警告，减少日志量'''
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

'''用户登录'''
def xinstorlogin():
    loginheaders = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Authorization': 'null',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Host': common.testhost,
        'Origin': common.testurl,
        'Referer': common.testurl
    }
    loginbody = {
        'username': common.testuser,
        'password': common.testpass
    }

    loginurl = common.testurl + '/api/auth/'
    testlogin = requests.post(loginurl, data=loginbody, json=loginheaders, verify=False)
    if (testlogin.status_code != 201):
        assert (False), "Login Failed"
    return testlogin

'''创建块存储卷'''
def createvolume(myauth, myxspdc, poolname, volumename, size):
    volumeheaders = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Host': common.testhost,
        'Origin': common.testurl,
        'Referer': common.testurl,
        'Authorization': myauth,
        'xspdc': myxspdc
    }
    volumebody = {
        'cipher_block_size': 4096,
        'cipher_key_count': 4,
        'cipher_type': '2',
        'max_bytes': {},
        'need_encrypt': '0',
        'pool': poolname,
        'image': volumename,
        'size': size
    }
    volumeurl = common.testurl + '/api/iscsi/disk'
    tesetcreatevolume = requests.post(volumeurl, json=volumebody, headers=volumeheaders, verify=False)
    if (tesetcreatevolume.status_code != 201):
        assert (False), "Create Volume Failed"
    return tesetcreatevolume

'''创建存储池'''
def createpool(myauth, myxspdc, groupname, poolname, maxbytes):
    poolheaders = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Host': common.testhost,
        'Origin': common.testurl,
        'Referer': common.testurl,
        'Authorization': myauth,
        'xspdc': myxspdc
    }

    poolbody = {
        "pool_name": poolname,
        "devicegroup": groupname,
        "failure_domain": "osd",
        "size": 2,
        "pool_type": "replicated",
        "osd_num": 2,
        "k_value": 2,
        "m_value": 1,
        "max_bytes": maxbytes
    }
    poolurl = common.testurl + '/api/pools'
    tesetcreatepool = requests.post(poolurl, json=poolbody, headers=poolheaders, verify=False)
    if (tesetcreatepool.status_code != 201):
        assert (False), "Create Pool Failed"
    return tesetcreatepool

'''获取已有的存储池'''
def getpool(myauth, myxspdc):
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Host': common.testhost,
        'Origin': common.testurl,
        'Referer': common.testurl,
        'Authorization': myauth,
        'xspdc': myxspdc
    }
    parameters = {
        "fields": 'pool_name,type,reliability_level,create_time,status,dg_name,ec_info,size,max_bytes,stats,applications'
    }
    poolurl = common.testurl + '/api/pools'
    testgetpool = requests.get(poolurl, params=parameters, headers=headers, verify=False)
    if (testgetpool.status_code != 200):
        assert (False), "Get Pool Failed"
    return testgetpool

'''创建用户
role : system/security/audit
'''
def createuser(myauth, myxspdc, account, name, role, phone, email):
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Host': common.testhost,
        'Origin': common.testurl,
        'Referer': common.testurl,
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
    poolurl = common.testurl + '/api/operator'
    testcreate = requests.post(poolurl, json=parameters, headers=headers, verify=False)
    return testcreate

'''创建机架
'''
def createrack(myauth, myxspdc, rackname):
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Host': common.testhost,
        'Origin': common.testurl,
        'Referer': common.testurl,
        'Authorization': myauth,
        'xspdc': myxspdc
    }
    parameters = {
        "name": rackname,
        "type": 'rack',
        "host": []
    }
    poolurl = common.testurl + '/api/topology'
    testcreate = requests.post(poolurl, json=parameters, headers=headers, verify=False)
    return testcreate

'''创建客户端'''
def creatclient(myauth, myxspdc, target_iqn, client_iqn):
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Host': common.testhost,
        'Origin': common.testurl,
        'Referer': common.testurl,
        'Authorization': myauth,
        'xspdc': myxspdc
    }
    parameters = {
        "client_iqn": client_iqn,
         "target_iqn": target_iqn
    }
    poolurl = common.testurl + '/api/iscsi/client'
    testcreate = requests.post(poolurl, json=parameters, headers=headers, verify=False)
    return testcreate