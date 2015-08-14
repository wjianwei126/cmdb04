from django.conf.urls import patterns, include, url
from django.contrib import admin
from web.user_views import *
from web.viewsetsall import *
from rest_framework import routers,serializers,viewsets



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cmdb04.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^adduser/', useadd_by_form,name='adduserurl'),
    url(r'^getuserlist/', getuserlist,name='listuserurl'),
    url(r'^deluser/(\d+)', deluser),
    url(r'^update_user_info/(\d+)', update_user_info,name='updateuserinfo'),
    url(r'^changepwd/', changepwd,name='changepasswd'),
    url(r'^resetpwd/(\d+)', reset_password,name='resetpwd'),
    url(r'^loginout/', loginout),
    url(r'^checkoldpasswd/', checkoldpasswd,name='checkoldpasswd'),
    url(r'^timer/', timer),
)
