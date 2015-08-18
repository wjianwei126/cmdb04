from django.conf.urls import patterns, include, url
from web.encoder_views import *


urlpatterns = patterns('',
    url(r'^getencoderstatus/', getencoderstatus,name='getencoderstatus'),
    url(r'^addencoderstatus/', output_status_add_by_form,name='addencoderstatus'),
    url(r'^encoderstatus/(\w+)', encoderstatus,name='encoderstatus'),
    url(r'^archcpustatus/', archcpustatus,name='archcpustatus'),
    url(r'^archencoderstatus/', archcpustatus,name='archencoderstatus'),
    url(r'^archcpustatusajax/', archcpustatusajax,name='archcpustatusajax'),
    url(r'^archmemstatusajax/',archmemstatusajax,name='archmemstatusajax'),
    url(r'^encoderhandle/', encoderhandle,name='encoderhandle'),
    url(r'^encoderhandleajax/', encoderhandleajax,name='encoderhandleajax'),


)