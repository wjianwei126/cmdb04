#!/usr/bin/env python
# coding:utf-8
#Created by Hisen on 2015/5/29
import re
pattern = re.compile(ur'(\d+)\.(\d+)\.(\d+)\.(\d+)')
str = u'127.0.0.1:8888'
print(pattern.search(str))