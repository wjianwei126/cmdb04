#!/usr/bin/env python
# coding:utf-8
#Created by Hisen on 2015/6/15

from django import forms

class Fippostion(forms.Form):
    ip = forms.EmailField(required=True,label=u'',widget=forms.PasswordInput(attrs={'placeholder':u'请输入要查询的IP地址','class' : 'form-control'}))