from django.conf.urls import patterns, include, url
from web.tools_views import *



urlpatterns = patterns('',
    url(r'^ippostion/', ippostion,name='ippostion'),
    url(r'^ippostionaj/', ippostionaj,name='ippostionaj'),
    url(r'^timestamp/', timestamp,name='timestamp'),
)
