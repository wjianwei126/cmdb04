from django.conf.urls import patterns, include, url
from web.live_views import *



urlpatterns = patterns('',
    url(r'^getlivepics/(\d+)', getlivepics,name='getlivepics'),
    url(r'^getlivelist/(\d+)', getlivelist,name='getlivelist'),
    url(r'^createlivepics/', createlivepics,name='createlivepics'),
    url(r'^channeslencoder/(\w+)', channeslencoder,name='channeslencoder'),
    url(r'^ytcentercdn/', ytcentercdn,name='ytcentercdn'),
    url(r'^addcdnnode/', addcdnnode,name='addcdnnode'),
    url(r'^cdnnodelist/', cdnnodelist,name='cdnnodelist'),
    url(r'^delcdnnode/(\d+)', delcdnnode,name='delcdnnode'),
    url(r'^enchajax/', enchajax,name='enchajax'),
)
