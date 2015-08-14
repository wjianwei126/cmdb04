#!/usr/bin/env python
# coding:utf-8
#Created by Hisen on 2015/2/4.
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from web.models import Asset
class loginforms(ModelForm):

    def __init__(self, *args, **kwargs):
        super(loginforms, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control','placeholder':'username'})
        self.fields['username'].label = ''      #清除自带 label
        self.fields['username'].help_text = ''  #清除自带 help 信息
        self.fields['username'].error_messages['required'] = u'用户名不能为空'
        self.fields['password'].widget_attrs(forms.PasswordInput(attrs={'onclick':'return false;'}))
        self.fields['password'].widget.attrs.update({'class' : 'form-control','placeholder':'password'})
        self.fields['password'].error_messages['required'] = u'密码不能为空'
        self.fields['password'].label = ''
    class Meta:
        model = User
        fields = ['username', 'password']
        #password = forms.CharField(widget=forms.PasswordInput())
        #widgets = {
        #    'password': forms.PasswordInput()
        #}
        #password.label = ''
        # widgets 是html页面显示的样式 下面widgets意思是 将 password 字段 在HTML中 显示为密码输入 而非判断输入是否合法
        #
        '''There's a distinction between form fields and form widgets.
        You can think about it this way -- The form field decides how python should work with the field (validation, type, etc).
        The form widget is the HTML representation.
        In your case you want to deal with character input, but you want the HTML to show a password input.'''
        widgets = {
            'password': forms.PasswordInput(),
        }