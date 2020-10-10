# -*- coding: utf-8 -*-
import requests
'''
关闭当前节点dsm-agent进程自动拉起mon、mgr、iscsigw服务接口
False为开启，True为关闭。
在/var/log/dsm-agent.log查看操作结果
'''
body = {
    "mon": "True",
    "mgr": "True",
    "iscsigw": "True",
}
url = 'https://192.168.225.189:9000/service_watcher/service_filter'
close = requests.post(url, json=body, verify=False)
print (close.json())


