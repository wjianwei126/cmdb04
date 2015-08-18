#!/usr/bin/env python
# coding:utf-8
# Created by Hisen on 2015/8/18
import os
import re



def snmpgetcpudata(host,key,oid):
    cmd = 'snmpwalk %s -v 2c -c %s %s'%(host,key,oid)
    #result = re.findall(r'\"([^"]+)\"',str(os.popen(cmd).read()))[0]
    result = str(os.popen(cmd).read()).split(':')[1].strip()
    result = 100 - int(result)
    return result
def snmpgetmemdata(host,key):
    usecmd = 'snmpwalk %s -v 2c -c %s .1.3.6.1.4.1.2021.4.6.0'%(host,key)
    allcmd = 'snmpwalk %s -v 2c -c %s .1.3.6.1.4.1.2021.4.5.0'%(host,key)
    useresult = str(os.popen(usecmd).read()).split(':')[1].strip()
    allresult = str(os.popen(allcmd).read()).split(':')[1].strip()
    result = float(useresult) / int(allresult)
    result =  '%.2f' %(float(result) * 100)
    allmem = float(allresult) / 1024
    return result,allmem