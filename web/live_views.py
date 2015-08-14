#!/usr/bin/env python
# coding:utf-8
# Created by Hisen on 2015/4/12
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from multiprocessing import Process, Pool
from web.models import tvie_channels
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from createlivepics import createpics
from watermark import addwatermark
import mysql_conn
import urllib,urllib2
import simplejson as json
from web.forms.form_for_addcdnnode import CdnAddForm
from web.models import cdnnode
from web.models import MyUser as User
from web.taobaoip import taobaoip_cityisp
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from web import stream_twtest as stream_test
from enhandle import enhandle
from django_ajax.decorators import ajax


def createlivepics(request):
    #contents = tvie_channels.objects.all()
    contents = tvie_channels.objects.filter(server_group='直播服务器01')
    p = Pool(processes=5)
    for line in contents:
        stream = line.stream
        cln = str(stream).strip('\n').strip('')
        name = str(stream).split('/')[-2]
        cmd = "/usr/local/ffmpeg/bin/ffmpeg -probesize 32768  -i %s -y -t 0.001 -ss 1 -f image2 -r 1 /djangoproject/cmdb04-dev/cmdb04/statics/livepics/%s.jpg"%(cln,name)
        #result = createpics(cmd,3)
        p.apply_async(createpics,[cmd,5])
    p.close()
    for line in contents:
        stream = line.stream
        name = str(stream).split('/')[-2]
        addwatermark(name)
    return render_to_response('live/livemonitor.html')
def getlivepics(requset,id):
    allch={}
    ID = id
    if ID == '1':
        server_group_id = '直播服务器01'
    elif ID == '2':
        server_group_id = '直播服务器02'
    elif ID == '3':
        server_group_id = '直播服务器03'
    contents = tvie_channels.objects.filter(server_group=server_group_id)
    for line in contents:
        stream = line.stream
        chann = line.channels
        name = str(stream).split('/')[-2]
        allch[name]=[stream,chann]
    channid = ID
    return render_to_response('live/livemonitor.html',locals())
@login_required()
def getlivelist(request,id):
    searchstr = request.REQUEST.get('findchannel','None')
    ID = id
    if ID == '4':
        if searchstr != 'None':
            sql = "SELECT channels.id,channels.display_name,channels.channel_name, servers.name,servers.ip_address,servers.host_name,streams.`name`,streams.uri FROM channels,servers,streams  WHERE channels.server_id = servers.id and channels.type = 'live' and channels.`status` <> 'DELETED' and  channels.id = streams.channel_id and streams.`status` = 'NORMAL' AND   concat(display_name, channel_name,uri) LIKE '%%%s%%' order by LENGTH (channels.id),channels.id;"%searchstr
            contents,counts = mysql_conn.mysql_handle(sql)
            http_status_input = stream_test.stream_test_input(contents)
            http_status_output = stream_test.stream_test_output(contents)
            return render_to_response('live/channelslist.html',locals())
        else:
            sql = "SELECT channels.id,channels.display_name,channels.channel_name, servers.name,servers.ip_address,servers.host_name,streams.`name`,streams.uri FROM channels,servers,streams  WHERE channels.server_id = servers.id and channels.type = 'live' and channels.`status` <> 'DELETED' and  channels.id = streams.channel_id and streams.`status` = 'NORMAL'  order by LENGTH (channels.id),channels.id;"
            contents,counts = mysql_conn.mysql_handle(sql)
            http_status_input = stream_test.stream_test_input(contents)
            http_status_output = stream_test.stream_test_output(contents)
            return render_to_response('live/channelslist.html',locals())
    else:
        if searchstr != 'None':
            sql = "SELECT channels.id,channels.display_name,channels.channel_name, servers.name,servers.ip_address,servers.host_name,streams.`name`,streams.uri FROM channels,servers,streams  WHERE channels.server_id = servers.id and channels.type = 'live' and channels.`status` <> 'DELETED' and servers.name='server%s' and channels.id = streams.channel_id and streams.`status` = 'NORMAL' AND   concat(display_name, channel_name,uri) LIKE '%%%s%%' order by servers.name,channels.id;"%(ID,searchstr)
            contents,counts = mysql_conn.mysql_handle(sql)
            http_status_input = stream_test.stream_test_input(contents)
            http_status_output = stream_test.stream_test_output(contents)
            return render_to_response('live/channelslist.html',locals())
        else:
            sql = "SELECT channels.id,channels.display_name,channels.channel_name, servers.name,servers.ip_address,servers.host_name,streams.`name`,streams.uri FROM channels,servers,streams  WHERE channels.server_id = servers.id and channels.type = 'live' and channels.`status` <> 'DELETED' and servers.name='server%s' and channels.id = streams.channel_id and streams.`status` = 'NORMAL'  order by servers.name,channels.id;"%ID
            contents,counts = mysql_conn.mysql_handle(sql)
            http_status_input = stream_test.stream_test_input(contents)
            http_status_output = stream_test.stream_test_output(contents)
            return render_to_response('live/channelslist.html',locals())
@login_required()
def channeslencoder(requset,key):
    #显示全部
    if key == 'all':
        sql = "select channels.display_name,streams.uri from channels ,streams  where channels.id=streams.channel_id and streams.uri like '%channels%' and streams.status = 'NORMAL' order BY LENGTH(uri),uri"
        contents,counts = mysql_conn.mysql_handle(sql)
    #只显示发布的频道
    elif key == 'publish':
        sql = "select channels.display_name,streams.uri from channels ,streams  where channels.id=streams.channel_id and streams.uri like '%channels%' and streams.status = 'NORMAL' AND channels.status = 'ACTIVE' order BY LENGTH(uri),uri"
        contents,counts = mysql_conn.mysql_handle(sql)
    return render_to_response('live/channelencoder.html',locals())
@login_required()
def ytcentercdn(request):

    citylist={}
    contents = cdnnode.objects.all()
    for line in contents:
        position = line.position.decode('utf-8')[:-1].encode('utf-8')
        if citylist.has_key(line.company):
            companylist = citylist[line.company]
            if companylist.count(position) == 0:
               companylist.append(position)
            citylist[line.company] = companylist
        else:
            citylist[line.company] = [position]
    return render_to_response('live/centertocdnmap.html',locals())
def addcdnnode(request):
    if request.method == 'POST':
        data=request.POST
        nodeform=CdnAddForm(data)
        if nodeform.is_valid():
           ipmessage=nodeform.save(commit=False) #代表不要提交到数据库，然后会返回一个class，然后对实例的password属性赋值
           ip = nodeform.cleaned_data['ip']
           company = nodeform.cleaned_data['company']
           position,isp = taobaoip_cityisp(ip)
           position.encode('utf-8')
           isp.encode('utf-8')
           ipmessage.position=position
           ipmessage.isp =isp
           nodeform.save()
           model=nodeform
           return  render_to_response('live/addcdnnode.html',locals(),context_instance=RequestContext(request))
        else:
            model=nodeform
            return render_to_response('live/addcdnnode.html',locals(),context_instance=RequestContext(request))
    model = CdnAddForm()
    return render_to_response('live/addcdnnode.html',locals(),context_instance=RequestContext(request))
@login_required()
def cdnnodelist(request,):
    searchstr = request.REQUEST.get('findnode','None')
    if searchstr != 'None':
       searchstr = request.GET['findnode']
       contents = cdnnode.objects.filter(Q(company__contains=searchstr)|Q(ip__contains=searchstr)|Q(position__contains=searchstr)|Q(isp__contains=searchstr)).order_by('id')
       counts = contents.count()
       issearch = 'true'
       searchstr = searchstr
       return render_to_response('live/cdnnodelist.html',locals())
    else:
        loginuser = request.user.username
        superusercheck=User.objects.filter(username=loginuser)
        counts = cdnnode.objects.count()
        for line in superusercheck:
            if line.is_superuser is True:
               contents = cdnnode.objects.all().order_by('id')
               superusercheck = '1'
            else:
               superusercheck = '0'
        return render_to_response('live/cdnnodelist.html',locals())
@login_required()
def delcdnnode(request,id):
    node = cdnnode.objects.get(id=id)
    node.delete()
    obj_url = request.META.get('HTTP_REFERER')  #删除后，返回到原删除页，防止在page2删除后，跳到page1.
    return HttpResponseRedirect(obj_url)


@ajax()
def enchajax(request):
    snum=request.POST.get('snum')
    hnum=request.POST.get('hnum')
    sql = "SELECT uri FROM streams WHERE channel_id = '%s'"%snum
    contents,counts = mysql_conn.mysql_handle(sql)
    for line in contents:
        s1 = str(line).find('110') #提取服务器IP
        e1 = str(line).find('/channels')
        s2 = str(line).find('w/') #提取编码器通道
        e2 = str(line).find('/f')
        snumf = str(line)[s1+4:e1]
        tnumf = str(line)[s2+2:e2]
    status = enhandle(snumf,tnumf,hnum)
    return {'status_code':status}