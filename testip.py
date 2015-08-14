#!/usr/bin/env python
# coding:utf-8
# Created by Hisen on 2015/8/5
import os
output = os.popen('fping -u -A -r 1 172.16.110.214')
print len(output.read())
