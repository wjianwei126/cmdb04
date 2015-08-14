#!/usr/bin/env python
# coding:utf-8
# Created by Hisen on 2015/6/28
# 由于流断掉之后还有可能存在内容,导致的http状态仍未200,现改为判断两次m3u8文件的m3u8 md5是否一致
import time
import requests
def stream_test_input(contents):
    http_status_input={}
    for line in contents:
        chid = str(line[0])
        churl = str(line[-1]).split()[0].replace('flv','m3u8',1)
        if 'm3u8' in churl and '172' in churl:
          try:
            r = requests.get(churl,timeout=2)
            m1 = r.content
            print m1
            time.sleep(0.5)
            r = requests.get(churl,timeout=2)
            m2 = r.content
            print m2
            if m1 == m2:
                http_status_input[chid]='404'
            else:
                http_status_input[chid]='%s'%r.status_code
          except Exception:
            http_status_input[chid]='timeout'
            continue
    return http_status_input
def stream_test_output(contents):
    http_status_out={}
    for line in contents:
       chid = str(line[0])
       #churl = str(line[-1]).split()[0].replace('flv','m3u8',1)
       churl = 'http://'+line[4]+'/channels/tvie/'+line[2]+'/m3u8:'+line[6]
       if 'm3u8' in churl and '172' in churl:
          try:
            r = requests.get(churl,timeout=2)
            http_status_out[chid]='%s'%r.status_code
          except Exception:
            http_status_out[chid]='timeout'
            continue
    return http_status_out