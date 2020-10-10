import requests


def login(url, userName, pwd):
    url = url
    url_list = url.split("//")
    ip = url_list[1]

    loginheaders = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Authorization': 'null',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Host': ip,
        'Origin': url,
        'Referer': url
    }
    loginbody = {
        'username': userName,
        'password': pwd
    }
    loginurl = url + '/api/auth/'
    testlogin = requests.post(loginurl, data=loginbody, json=loginheaders, verify=False)
    myAuth = testlogin.headers['Authorization']
    myxp = testlogin.json().get('data').get('xspdc')
    # print(testlogin.json())
    if (testlogin.status_code != 201):
        assert (False), "Login Failed"
    return myAuth, myxp


def CreateBackupTask(url, myauth, myxp, poolName, lunName, BaPoolName, days):
    url = url
    url_list = url.split("//")
    ip = url_list[1]

    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Host': ip,
        'Origin': url,
        'Referer': url,
        'Authorization': myauth,
        'xspdc': myxp
    }

    post_url = url + "/api/image_bak/bak_config"
    parameters = {
        "pool": poolName, "image_list": [lunName], "bak_sys_id": 53,
        "bak_pool": BaPoolName, "save_time": days,
        "bak_period": 1,
        "time_range_start": "00:00",
        "time_range_end": "00:00",
        "bak_type": "rep",
        "data_encrypt": "off"
    }
    testcreate = requests.post(post_url, json=parameters, headers=headers, verify=False)
    return testcreate


response = login("https://192.168.170.120:18888", "admin", "Xit1234567")
print(response)

res = CreateBackupTask("https://192.168.170.120:18888", response[0], response[1], "GLOpool", "test1", "BaGLOpool", 7)
print(res.json())
