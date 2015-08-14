#!/usr/bin/env python
# coding:utf-8
# Created by Hisen on 2015/3/31
from django import forms
from web.models import cdnnode

class CdnAddForm(forms.ModelForm):
    class Meta:
        model = cdnnode
        fields = ['company','ip','note']
        widgets = {
            'company' : forms.TextInput(attrs={'class':'form-control'}),
            'ip' : forms.TextInput(attrs={'class':'form-control'}),
            'note' : forms.Textarea(attrs={'class':'form-control'}),
        }
    def __init__(self,*args,**kwargs):
        super(CdnAddForm,self).__init__(*args,**kwargs)
        self.fields['company'].label=u'CDN'
        self.fields['company'].error_messages={'required':u'CDN厂家不能为空','invalid':u'CDN厂家格式错误,或者已存在'}
        self.fields['ip'].label=u'IP'
        self.fields['ip'].error_messages={'required':u'请输入IP','invalid':u'请输入有效IP'}
        self.fields['note'].label=u'备注'
        self.fields['note'].error_messages={'required':u'请输入备注','invalid':u'请输入有效IP'}