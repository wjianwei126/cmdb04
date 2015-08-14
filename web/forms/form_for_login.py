#!/usr/bin/env python
# coding:utf-8
#Created by Hisen on 2015/2/4.
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(required=True,label=u'',widget=forms.TextInput(attrs={'placeholder':u'username','class' : 'form-control'}))
    password = forms.CharField(required=True,label=u'',widget=forms.PasswordInput(attrs={'placeholder':u'password','class' : 'form-control'}))