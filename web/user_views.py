#coding:utf-8
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response
from django.http import  HttpResponse,JsonResponse
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
import  simplejson
import json

@login_required()
def index(request):
    #alldrivers = 100
    #raw_sql = 'SELECT hostname from web_asset,web_idc WHERE web_asset.idc_id = web_idc.id'
    idc_all = IDC.objects.all()
    loginuser = request.user.username
    return render_to_response('index.html',locals())
''''
#用于生成页面登陆表单
def LoginByForm(request):
    if request.method == 'POST':
        data=request.POST
        loginForm=LoginForm(data)
        if loginForm.is_valid():
           username=loginForm.cleaned_data['username']
           password=loginForm.cleaned_data['password']
           user = auth.authenticate(username=username,password=password)
           if user is not None:
               auth.login(request,user)
               obj_url = request.META.get('HTTP_REFERER')   #http://127.0.0.1:8888/accounts/login/?next=/busadmin/add_server/
                                                            #为了登陆后能跳转到next之后的链接
               if obj_url.count('next') == 1:
                  url2=obj_url.split('=')[1]
                  return HttpResponseRedirect('%s' %url2)
               else:
                   return HttpResponseRedirect('/index/')
           else:
                password_is_wrong = True
                model = LoginForm()
                return render_to_response('login.html',locals(),context_instance=RequestContext(request))

        else:
            return render_to_response('login.html',{'model':loginForm},context_instance=RequestContext(request))
    loginForm = LoginForm()
    return render_to_response('login.html',{'model':loginForm},context_instance=RequestContext(request))
'''
#新登陆页面
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print username
        print password
        user = auth.authenticate(username=username,password=password)
        if user is not None:
               auth.login(request,user)
               obj_url = request.META.get('HTTP_REFERER')   #http://127.0.0.1:8888/accounts/login/?next=/busadmin/add_server/
                                                            #为了登陆后能跳转到next之后的链接
               if obj_url.count('next') == 1:
                  url2=obj_url.split('=')[1]
                  return HttpResponseRedirect('%s' %url2)
               else:
                   return HttpResponseRedirect('/index/')
        else:
            password_is_wrong = True
            #return render_to_response('login.html',locals(),context_instance=RequestContext(request))
            return HttpResponseRedirect('/login/')
    else:
        return  render_to_response('login.html',locals(),context_instance=RequestContext(request))

#用户注销
def loginout(request):
    user = request.user
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')
#用于生成页面添加用户表单
def useadd_by_form(request):
    result={'addResult':''}
    if request.method == 'POST':
        data=request.POST
        userForm=UserAddForm(data)
        if userForm.is_valid():
           check_user1=User.objects.filter(username=userForm.cleaned_data['username'])
           if len(check_user1) > 0:
               adduserresult='addexits'
               model=userForm
               return  render_to_response('user/adduser.html',locals(),context_instance=RequestContext(request))
           else:
               #利用models存储信息
               user=userForm.save(commit=False) #代表不要提交到数据库，然后会返回一个class，然后对实例的password属性赋值
               user.set_password('123456') #新建用户默认密码123456
               userForm.save()
               check_username=User.objects.filter(username=userForm.cleaned_data['username']) #验证是否加到数据库
               if len(check_username) > 0:
                    adduserresult='addsuccess'
                    model=userForm
           return  render_to_response('user/adduser.html',locals(),context_instance=RequestContext(request))
        else:
            model=userForm
            return render_to_response('user/adduser.html',locals(),context_instance=RequestContext(request))
    model = UserAddForm()
    return render_to_response('user/adduser.html',locals(),context_instance=RequestContext(request))

#获取用户列表
@login_required()
def getuserlist(request):
    loginuser = request.user.username
    superusercheck=User.objects.filter(username=loginuser)
    usercounts = User.objects.count()
    for line in superusercheck:
        if line.is_superuser is True:
           contents = User.objects.all()
           superusercheck = '1'
        else:
           superusercheck = '0'
    return render_to_response('user/userlist.html',locals())

#删除用户
@login_required()
def deluser(request,id):
    ID=id
    try:
        user = User.objects.get(id=ID)
        loginuser = request.user.username
        superusercheck=User.objects.filter(username=loginuser)[0]#会返回一个列表 由于只是判断用户名是否为用户名，过滤的又是唯一用户，直接取[0]
        if superusercheck.is_superuser is True:
           user.delete()
           contents = User.objects.all()
           loginuser=request.user.username
           delresult='delsuccess'
           obj_url = request.META.get('HTTP_REFERER')  #删除后，返回到原删除页，防止在page2删除后，跳到page1.
           return HttpResponseRedirect(obj_url)
           #return render_to_response('userlist.html',locals(),context_instance=RequestContext(request))
        else:
            superusercheck = '0'
            return render_to_response('user/userlist.html',locals(),context_instance=RequestContext(request))
    except:
        loginuser = request.user.username
        superusercheck=User.objects.filter(username=loginuser)[0]#会返回一个列表 由于只是判断用户名是否为用户名，过滤的又是唯一用户，直接取[0]
        if superusercheck.is_superuser is True:
            loginuser=request.user.username
            resetresult='iderror'  #页面 resetresult 和 delresult实际是一个
            contents = User.objects.all()
            return render_to_response('user/userlist.html',locals(),context_instance=RequestContext(request))
        else:
            loginuser=request.user.username
            superusercheck = '0'
            return render_to_response('user/userlist.html',locals(),context_instance=RequestContext(request))

#更新用户信息
@login_required()
def update_user_info(request,ID):
    obj_url = request.META.get('HTTP_REFERER')
    user = User.objects.get(id = ID)
    ori_username = user.username  #前端已经限制修改用户名，防止通过修改前端手段post更改的用户名
    if request.method=='POST':
        form = UserUpdateForm(request.POST,instance=user)
        #form = UserUpdateForm(initial={'username':user.username,'email':user.email,'nickname':user.nickname,'sex':user.sex,'is_superuser':user.is_superuser,'is_active':user.is_active})
        if form.is_valid():
            form.save(commit=False)
            user.username = ori_username #前端已经限制修改用户名，防止通过修改前端手段post更改的用户名
            form.save()
            #return HttpResponseRedirect(reverse('listuserurl'))
            #obj_url = request.META.get('HTTP_REFERER')  #删除后，返回到原删除页，防止在page2删除后，跳到page1.
            return HttpResponseRedirect(obj_url)
        else:
            pass
    else:
        form = UserUpdateForm(instance=user
        )

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('user/update_user_info.html',kwvars,RequestContext(request))
@login_required()
def checkoldpasswd(request):
    username = request.user.username
    oldpasswd = request.POST.get('oldpassword')
    user = auth.authenticate(username=username, password=oldpasswd)
    if user is not None:
        error_dict = 0
        return HttpResponse(error_dict)
    else:
        error_dict = 1
        return HttpResponse(error_dict)
####模态框修改密码####
@login_required()
def changepwd(request):
    username = request.user.username
    oldpasswd = request.POST.get('oldpassword')
    newpasswd = request.POST.get('newpassword1')
    newpasswd2 = request.POST.get('newpassword2')
    user = auth.authenticate(username=username, password=oldpasswd)
    if user is not None: #验证老密码
        if newpasswd == newpasswd2: #判断两次密码是否相同
           user.set_password(newpasswd2)
           user.save()
           auth.logout(request)
    else:
        return HttpResponse('原密码错误')
#重置用户密码
def reset_password(request,id):
    ID = id
    #loginuser=request.user.username
    user = User.objects.get(id=ID)
    user.set_password('123456')
    user.save()
    obj_url = request.META.get('HTTP_REFERER')  #删除后，返回到原删除页，防止在page2删除后，跳到page1.
    return HttpResponseRedirect(obj_url)




def piliang2(request):
     tmp1 = random.random()
     tmp2 = hashlib.md5(str(tmp1)).hexdigest()
     add=User.objects.create_user(username=str(tmp2),password='tom2',email='tom@qq.com')
     add.save()
     return  HttpResponse('1111111111')

def timer(request):
    return render_to_response('encoders/timer.html')
