#!/usr/bin/env python
# coding:utf-8
# Created by Hisen on 2015/7/27
import requests
import re
def enhandle(num,tnum,hnum):
    s = requests.session()
    data = {'username':'admin','password':'tvie_rocks','update':'登录'}
    res=s.post('http://172.16.110.%s/mgmt/login'%num,data)
    if hnum == '1': #重启
       s.get("http://172.16.110.%s/mgmt/command!endChannel?channelId = %s"%(num,tnum))
       r = s.get("http://172.16.110.%s/mgmt/command!startChannel?channelId = %s"%(num,tnum))
    else:
       r = s.get("http://172.16.110.%s/mgmt/command!endChannel?channelId = %s"%(num,tnum))
    return r.status_code


