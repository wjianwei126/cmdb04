#!/usr/bin/env python
# coding:utf-8
# Created by Hisen on 2015/4/12
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.shortcuts import render_to_response,RequestContext
from django.http import  HttpResponse
from web.forms.form_for_ippostion import Fippostion
import urllib,urllib2
import simplejson as json
from web.taobaoip import taobaoip_all
from django_ajax.decorators import ajax
from web.models import ippostionhistory
import time

def ippostion(request):
       history = ippostionhistory.objects.all().order_by("-date")[:10]
       return render_to_response('tools/ippostion.html',locals(),context_instance=RequestContext(request))
@ajax()
def ippostionaj(request):
        ip=request.POST.get('ip')
        country,region,city,isp = taobaoip_all(ip)
        data={'ip':ip,'country':country,'region':region,'city':city,'isp':isp}
        date = time.strftime('%Y年%m月%d日 %H:%M:%S',time.localtime(time.time()))
        if len(country) != 0 and len(isp) != 0:
            check = ippostionhistory.objects.filter(ip=ip)
            if len(check) == 0:
               ippostionhistory.objects.create(ip=ip,country=country,region=region,city=city,isp=isp,date=str(date))
            else:
               check.update(date=str(date))
        history = ippostionhistory.objects.all().order_by("-date")[:10]
        historydata={}
        i = 0
        for line in history:
           i=i+1
           historydata[i] = {'ip':line.ip,'country':line.country,'region':line.region,'city':line.city,'isp':line.isp,'date':line.date}
           print i,line.date
        return {'data':data,'historydata':historydata}
def timestamp(request):
    return render_to_response('tools/timestamp.html')
