#!/usr/bin/env python
# coding:utf-8
# Created by Hisen on 2015/7/27
import requests
import re
s = requests.session()
data = {'username':'admin','password':'tvie_rocks','update':'登录'}
#post 换成登录的地址，
res=s.post('http://172.16.110.1/mgmt/login',data)
#a = s.get("http://172.16.110.1/mgmt/command!startChannel?channelId = 1")
#a = s.get("http://172.16.110.1/mgmt/command!endChannel?channelId = 1")
data2 = {'scriptSessionId':'EB7C599AE798F170951A792A0502450',
         'httpSessionId':'',
         'callCount':'1',
         'windowName':'',
         'c0-scriptName':'sysInfoService',
         'c0-methodName':'refreshSysInfo',
         'c0-id':'0',
         'page':'/mgmt/home.action',
         'c0-batchId':'1',
         'batchId':'2',
         }
a = s.post("http://172.16.110.1/mgmt/dwr/call/plaincall/sysInfoService.refreshSysInfo.dwr",data2)

result = str(a.text)

cpu = re.findall(r'\"([^"]+)\"',result)[3]
diskRate = re.findall(r'\"([^"]+)\"',result)[4]
memRate = re.findall(r'\"([^"]+)\"',result)[5]

print cpu,diskRate,memRate