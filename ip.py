#!/usr/bin/env python
# coding:utf-8
# Created by Hisen on 2015/8/5

f = file('ip.txt','w+')
for i in range(1,33):
    f.write('172.16.110.%s'%i+'\n')
f.close()
