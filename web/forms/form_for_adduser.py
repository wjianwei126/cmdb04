#!/usr/bin/env python
#coding:utf-8
from django import forms
from web.models import MyUser as User

class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        #exclude = ['id','last_login','password'] 排除这三个
        fields = ['username','email','sex','nickname','is_active','is_superuser']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'nickname' : forms.TextInput(attrs={'class':'form-control'}),
            'sex' : forms.Select(choices=((u'男', u'男'),(u'女', u'女')),attrs={'class':'form-control'}),
            'is_active' : forms.Select(choices=((True, u'启用'),(False, u'禁用')),attrs={'class':'form-control'}),
            'is_superuser' : forms.Select(choices=((True, u'是'),(False, u'否')),attrs={'class':'form-control'}),
        }
    def __init__(self,*args,**kwargs):
        super(UserAddForm,self).__init__(*args,**kwargs)
        self.fields['username'].label=u'用户名'
        self.fields['username'].error_messages={'required':u'用户名不能为空','invalid':u'用户名格式错误,或者已存在'}
        self.fields['email'].label=u'邮 箱'
        self.fields['email'].error_messages={'required':u'请输入邮箱','invalid':u'请输入有效邮箱'}
        self.fields['nickname'].label=u'别名'
        self.fields['nickname'].error_messages={'required':u'请输入姓名'}
        self.fields['sex'].label=u'性 别'
        self.fields['sex'].error_messages={'required':u'请选择性别'}
        self.fields['is_active'].label=u'状 态'
        self.fields['is_superuser'].label=u'管理员'