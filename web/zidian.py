#!/usr/bin/env python
# coding:utf-8
# Created by Hisen on 2015/6/16

dic={}
for i in range(100):
    dic['%s'%i]='111'
for k,v in dic.items():
    print k