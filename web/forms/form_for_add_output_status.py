#!/usr/bin/env python
# coding:utf-8
# Created by Hisen on 2015/3/31
from django import forms
from web.models import MyUser as User
from web.models import EencoderStatus

class OutputAddForm(forms.ModelForm):
    class Meta:
        encoders_choices = (
        ('encoder01', u'encoder01'),
        ('encoder02', u'encoder02'),
        ('encoder03', u'encoder03'),
        ('encoder04', u'encoder04'),
        ('encoder05', u'encoder05'),
        ('encoder06', u'encoder06'),
        ('encoder07', u'encoder07'),
        ('encoder08', u'encoder08'),
        ('encoder09', u'encoder09'),
        ('encoder10', u'encoder10'),
        ('encoder11', u'encoder11'),
        ('encoder12', u'encoder12'),
        ('encoder13', u'encoder13'),
        ('encoder14', u'encoder14'),
        ('encoder15', u'encoder15'),
        ('encoder16', u'encoder16'),
        ('encoder17', u'encoder17'),
        ('encoder18', u'encoder18'),
        ('encoder19', u'encoder19'),
        ('encoder20', u'encoder20'),
        ('encoder21', u'encoder21'),
        ('encoder22', u'encoder22'),
        ('encoder23', u'encoder23'),
        ('encoder24', u'encoder24'),
        ('encoder25', u'encoder25'),
        ('encoder26', u'encoder26'),
        ('encoder27', u'encoder27'),
        ('encoder28', u'encoder28'),
        ('encoder29', u'encoder29'),
        ('encoder30', u'encoder30'),
        ('encoder31', u'encoder31'),
        ('encoder32', u'encoder32'),
    )
        output_choice = (
        ('1', '通道1'),
        ('2', '通道2'),
        (3, '通道3'),
        (4, '通道4'),
        (5, '通道5'),
        (6, '通道6'),
        (7, '通道7'),
        (8, '通道8'),
    )
        model = EencoderStatus
        #exclude = ['id','last_login','password'] 排除这三个
        fields = ['encoder_name','output_name']
        widgets = {
            'encoder_name' : forms.Select(choices=encoders_choices,attrs={'class':'form-control'}),
            'output_name' : forms.CheckboxSelectMultiple(choices=output_choice,),
           # 'is_superuser' : forms.Select(choices=((True, u'是'),(False, u'否')),attrs={'class':'form-control'}),
        }
    def __init__(self,*args,**kwargs):
        super(OutputAddForm,self).__init__(*args,**kwargs)
        self.fields['encoder_name'].label=u'编码器'
        self.fields['encoder_name'].error_messages={'required':u'用户名不能为空','invalid':u'用户名格式错误,或者已存在'}
        self.fields['output_name'].label=u'通道名称'
        #self.fields['output_name'].error_messages={'required':u'请输入邮箱','invalid':u'请输入有效邮箱'}