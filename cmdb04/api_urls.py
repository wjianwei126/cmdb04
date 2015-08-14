from django.conf.urls import patterns, include, url
from django.contrib import admin
from web.user_views import *
from web.viewsetsall import *
from rest_framework import routers,serializers,viewsets



version = 'v1.0'

router = routers.DefaultRouter()
router.register(r'idc', IDCViewSet)
router.register(r'server', ServerViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auto_cmdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),

)
