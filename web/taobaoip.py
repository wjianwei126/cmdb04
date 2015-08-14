#!/usr/bin/env python
# coding:utf-8
#Created by Hisen on 2015/5/21
import urllib,urllib2
import simplejson as json
def taobaoip_cityisp(ip):
    ip = ip
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip='+ip
    ck = 'cna=zSn7DCz5qU0CAduP7tsP23Ap; isg=1C717FD70D9834C48E40434D397E6994; t=116b0ad1eea2fbb508b25c5c7a64a3c6'
    headers = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2121.3 Safari/537.36", "Cookie" : ck }
    req = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(req, timeout=60)
    the_page = response.read()
    value = json.loads(the_page)
    data = value['data']
    city = str(data['city'])
    isp=str(data['isp'])
    if len(city) == 0:
       city = 'ci_null'
    if len(isp) == 0:
        isp = 'i_null'
   # city = city.decode('utf-8')[:-1].encode('utf-8')
    return city,isp
def taobaoip_all(ip):
    ip = ip
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip='+ip
    ck = 'cna=zSn7DCz5qU0CAduP7tsP23Ap; isg=1C717FD70D9834C48E40434D397E6994; t=116b0ad1eea2fbb508b25c5c7a64a3c6'
    headers = { "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2121.3 Safari/537.36", "Cookie" : ck }
    req = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(req, timeout=60)
    the_page = response.read()
    value = json.loads(the_page)
    data = value['data']
    country = str(data['country'])
    region = str(data['region'])
    city = str(data['city'])
    isp=str(data['isp'])
    if len(country) == 0:
       country = 'c_null'
    if len(region) == 0:
       region = 'r_null'
    if len(city) == 0:
       city = 'ci_null'
    if len(isp) == 0:
       isp = 'i_null'
    return country,region,city,isp