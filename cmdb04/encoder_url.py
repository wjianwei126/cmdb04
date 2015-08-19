from django.conf.urls import patterns, include, url
from web.encoder_views import *


urlpatterns = patterns('',
    url(r'^addencoderstatus/', output_status_add_by_form,name='addencoderstatus'),
    url(r'^encoderstatus/(\w+)', encoderstatus,name='encoderstatus'),
    url(r'^tvieencoderstatus/', tvieencoderstatus,name='tvieencoderstatus'),
    url(r'^tviecpustatusajax/', tviecpustatusajax,name='tviecpustatusajax'),
    url(r'^tviememstatusajax/',tviememstatusajax,name='tviememstatusajax'),
    url(r'^tviediskstatusajax/',tviediskstatusajax,name='tviediskstatusajax'),
    url(r'^encoderhandle/', encoderhandle,name='encoderhandle'),
    url(r'^encoderhandleajax/', encoderhandleajax,name='encoderhandleajax'),


)