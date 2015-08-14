from django.conf.urls import patterns, include, url
from web.server_views import *



urlpatterns = patterns('',
    url(r'^addserver/', serveradd_by_form),
    url(r'^getserverlist/', getserverlist,name='getserverlist'),
    url(r'^getservermap/', getservermap,name='getservermap'),
    #url(r'^deluser/(\d+)', deluser),
    #url(r'^changepwd/', changepwd),

)
