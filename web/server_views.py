#coding:utf-8
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response
from django.http import  HttpResponse
import time
from  django.contrib import auth
#from django.contrib.auth.models import User
from web.models import MyUser as User
import random
import hashlib
# Create your views here.
from  django.contrib.auth import get_user_model
#from django.db import models
from web.models import IDC,Asset
from forms.form_for_login import LoginForm
from forms.form_for_adduser import UserAddForm
from forms.form_for_change_passwd import ChangePwdForm
from forms.form_for_update_user import UserUpdateForm

from django.template.context import RequestContext
from  django.http import  HttpResponseRedirect

import os

@login_required()
def getserverlist(request):
    loginuser = request.user.username
    superusercheck=User.objects.filter(username=loginuser)
    usercounts = User.objects.count()
    print usercounts
    for line in superusercheck:
        print line.is_superuser
        if line.is_superuser is True:
           contents = User.objects.all()
           superusercheck = '1'
        else:
           superusercheck = '0'
    userForm = UserAddForm()
    return render_to_response('server/addserver.html',locals())
@login_required()
def serveradd_by_form(requset):
    return render_to_response('server/addserver.html',locals())
@login_required()
def getservermap(request):
    pailist = range(1,3) #定义机柜总共排数
    guilist = range(1,11) #定义每排多少个机柜
    hanlist = range(1,16) #定义每个机柜可以放多少服务器
    file = 'jiguiceshi.txt'
    f = open(file,'r')
    data = {}
    for line in f.readlines():
        list = line.split()
        serip = list[1]
        seros = list[2]
        serloc = list[3]
        sersta = list[4]
        output = os.popen('fping -u -A -r 1 %s'%serip)
        result = len(output.read())
        if result != 0:
            sersta = 'down'
        else:
            sersta = 'up'
        data[list[0]] = [serip,seros,serloc,sersta]
    loginuser = request.user.username
    return  render_to_response('server/servermap.html',locals())