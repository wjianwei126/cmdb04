#!/usr/bin/env python
# coding:utf-8
#Created by Hisen on 2015/1/29.
from rest_framework import viewsets
from web.models import *
from web.serializersall import *

class IDCViewSet(viewsets.ModelViewSet):
    queryset =  IDC.objects.all()
    serializer_class = IDCSerializer
class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer