#!/usr/bin/env python
# coding:utf-8
# Created by Hisen on 2015/3/30
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
from django.core.urlresolvers import reverse
from forms.form_for_add_output_status import OutputAddForm

from django.template.context import RequestContext
from  django.http import  HttpResponseRedirect
from django_ajax.decorators import ajax
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response
from web.models import *
import simplejson
import mysql_conn
from enhandle import enhandle
from snmpgetdata import snmpgetcpudata,snmpgetmemdata

@login_required()
def getencoderstatus(request):
    loginuser = request.user.username
    data = { }
    contents = EencoderStatus.objects.order_by('encoder_name').all()
    encodercounts = EencoderStatus.objects.count()
    p = re.compile(r'\d+')
    for i in contents:
       #data[i.encoder_name.encode("utf-8")] = i.output_name.encode("utf-8")
       templist = i.output_name.encode("utf-8")
       t = p.findall(templist)
       data[i.encoder_name.encode("utf-8")] = t
    return render_to_response('encoders/encoderstatus.html',locals())


def output_status_add_by_form(request):
    if request.method=='POST':
        data=request.POST
        form = OutputAddForm(data)
        #form = UserUpdateForm(initial={'username':user.username,'email':user.email,'nickname':user.nickname,'sex':user.sex,'is_superuser':user.is_superuser,'is_active':user.is_active})
        if form.is_valid():
            output_name = form.cleaned_data['output_name']
            print output_name
            print type(output_name)
            form.save()
            #return HttpResponseRedirect(reverse('listuserurl'))
            #obj_url = request.META.get('HTTP_REFERER')  #删除后，返回到原删除页，防止在page2删除后，跳到page1.
            return HttpResponseRedirect(reverse('addencoderstatus'))
            #return HttpResponseRedirect('http://www.baidu.com')
        else:
            print '-------'
            print '输入不合法'
    else:
        form = OutputAddForm(
        )

    kwvars = {
        'form':form,
        'request':request,
    }

    return render_to_response('encoders/addencoderstatus.html',kwvars,RequestContext(request))
@login_required()
def encoderstatus(request,key):
    if key == 'all':
        sql = "select streams.uri from channels ,streams  where channels.id=streams.channel_id and streams.uri like '%channels%' and streams.status = 'NORMAL' order BY LENGTH(uri),uri"
        uri,counts_sql = mysql_conn.mysql_handle(sql)
    elif key == 'publish':
         sql = "select streams.uri from channels ,streams  where channels.id=streams.channel_id and streams.uri like '%channels%' and streams.status = 'NORMAL' and channels.`status` = 'ACTIVE' order BY LENGTH(uri),uri"
         uri,counts_sql = mysql_conn.mysql_handle(sql)
    data={}
    for line in uri:
        #一个频道对应1路流
        if str(line).count('http') == 1:
            id1 = str(line).split('/')[2].split('.')[-1]
            k1 = 'encoder%s'%id1
            var1 = str(line).split('/')[5]
            if data.has_key(k1):
               tmplist1 = data[k1]
               tmplist1.append('%s'%var1)
               data[k1] = tmplist1
            else:
               data[k1]=[var1]
        #一个频道对应2路流：ex:http://172.16.110.19/channels/preview/1/flv:500k http://172.16.110.28/channels/preview/1/flv:500k
        elif str(line).count('http') == 2:
            t = str(line).split(' ')#利用空格切成两条记录
            for m in range(len(t)):
               id2 = str(t[m]).split('/')[2].split('.')[-1] #获取ip结尾
               k2 = 'encoder%s'%id2 #生成encoder名称当做字典的key
               var2 = str(t[m]).split('/')[5]
               if data.has_key(k2):
                  tmplist2 = data[k2] #获取存在的列表
                  tmplist2.append('%s'%var2) #往列表添加内容,不用担心数据重复,因为前端会处理的
                  data[k2] = tmplist2 #添加完列表，再存入原字典
               else:
                  data[k2]=[var2] #以encoder名称存入字典{'encoder':['1']}
    contents = {}
    #用于在页面生成有序的encodername
    for i in range(1,33):
          contents[i]=['encoder%s'%i,'172.16.110.%s'%i]
    defaultstatus = []
    #生成列表供页面使用
    for i in range(1,9):
        defaultstatus.append(i)
    counts = 0
    for k,v in data.items():
        counts += len(set(data[k]))
    use_counts = counts
    nouse_counts = 160 - int(counts) - 8 #encoder7 encoder16 已经废掉
    return render_to_response('live/encoderstatus.html',locals())
def encoderhandle(request):
    key = 'handle'
    sql = "select streams.uri from channels ,streams  where channels.id=streams.channel_id and streams.uri like '%channels%' and streams.status = 'NORMAL' order BY LENGTH(uri),uri"
    uri,counts_sql = mysql_conn.mysql_handle(sql)
    data={}
    for line in uri:
        #一个频道对应1路流
        if str(line).count('http') == 1:
            id1 = str(line).split('/')[2].split('.')[-1]
            k1 = 'encoder%s'%id1
            var1 = str(line).split('/')[5]
            if data.has_key(k1):
               tmplist1 = data[k1]
               tmplist1.append('%s'%var1)
               data[k1] = tmplist1
            else:
               data[k1]=[var1]
        #一个频道对应2路流：ex:http://172.16.110.19/channels/preview/1/flv:500k http://172.16.110.28/channels/preview/1/flv:500k
        elif str(line).count('http') == 2:
            t = str(line).split(' ')#利用空格切成两条记录
            for m in range(len(t)):
               id2 = str(t[m]).split('/')[2].split('.')[-1] #获取ip结尾
               k2 = 'encoder%s'%id2 #生成encoder名称当做字典的key
               var2 = str(t[m]).split('/')[5]
               if data.has_key(k2):
                  tmplist2 = data[k2] #获取存在的列表
                  tmplist2.append('%s'%var2) #往列表添加内容,不用担心数据重复,因为前端会处理的
                  data[k2] = tmplist2 #添加完列表，再存入原字典
               else:
                  data[k2]=[var2] #以encoder名称存入字典{'encoder':['1']}
    contents = {}
    #用于在页面生成有序的encodername
    for i in range(1,33):
          contents[i]=['encoder%s'%i,'172.16.110.%s'%i]
    defaultstatus = []
    #生成列表供页面使用
    for i in range(1,9):
        defaultstatus.append(i)
    counts = 0
    for k,v in data.items():
        counts += len(set(data[k]))
    use_counts = counts
    nouse_counts = 160 - int(counts) - 8 #encoder7 encoder16 已经废掉
    return render_to_response('encoders/encoderhandle.html',locals())
#用于处理关闭重启通道，用来处理ajax传过来的内容
@ajax()
def encoderhandleajax(request):
    num=request.POST.get('num')
    tnum=request.POST.get('tnum')
    hnum=request.POST.get('hnum')
    print num,tnum,hnum
    enhandle(num,tnum,hnum)
    return {'status_code':'200'}
def archcpustatus(request):
    #result =snmpgetdata('localhost','public','.1.3.6.1.4.1.2021.10.1.3.1')
    return render_to_response('encoders/archencoderstatus.html',locals())
    #return HttpResponse(result)
@ajax()
def archcpustatusajax(request):
    hum = request.POST.get('hnum')
    result =snmpgetcpudata(hum,'public','.1.3.6.1.4.1.2021.11.11.0') #idle
    return result
@ajax()
def archmemstatusajax(request):
    hum = request.POST.get('hnum')
    result,allmem =snmpgetmemdata(hum,'public')
    return result,allmem