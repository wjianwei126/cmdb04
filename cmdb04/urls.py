from django.conf.urls import patterns, include, url
from django.contrib import admin
from web.user_views import *
from web.viewsetsall import *
import  user_urls
import server_urls
import encoder_url
import live_url
import tools_url
from rest_framework import routers,serializers,viewsets



urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include(user_urls)),
    url(r'^server/', include(server_urls)),
    url(r'^encoder/', include(encoder_url)),
    url(r'^live/', include(live_url)),
    url(r'^tools/', include(tools_url)),

    url(r'^index/',index),
    #url(r'^login/',LoginByForm,name='login'),
    url(r'^login/',login,name='login'),
    url(r'^accounts/login/',login),
    #url(r'^accounts/login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    url(r'^api/', include('cmdb04.api_urls')),
    url(r'^piliang2/', piliang2),


)
