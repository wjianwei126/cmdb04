#!/usr/bin/env python
# coding:utf-8
#Created by Hisen on 2015/1/29.
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from web.models import *

class IDCSerializer(serializers.HyperlinkedModelSerializer): #HyperlinkedModelSerializer意思是利用超链接的方式显示下一级内容
    class Meta:
        model = IDC
class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('id','sn','asset')
        depth = 2