from django.shortcuts import render, HttpResponse

from django import forms
from django.forms import fields

# Create your views here.

class TestForm(forms.Form):
    user = fields.CharField(
        widget=forms.TextInput(attrs={'n': 123}),   # 可以通过attrs来添加自定义属性
        required=True,
        max_length=10,
        min_length=3,
        error_messages={},
        label='用户名',
        initial='请输入用户名',
        # validators=[]
        # disabled=True,
        label_suffix='-->'
    )
    age = fields.IntegerField(
        required=True,
        label='年龄',
        max_value=200,
        min_value=1,
        error_messages={
            'max_value': '太大了',
        }
    )
    email = fields.EmailField()

    img = fields.FileField()

    # city = fields.ChoiceField(
    #     choices=[(1, '上海'), (2, '北京'), (3, '杭州'), ],
    #     initial=1,
    # )

    city = fields.TypedChoiceField(
        coerce=lambda x: int(x),
        choices=[(1, '上海'), (2, '北京'), (3, '杭州'), ],
        initial=1,
    )

    hobby = fields.MultipleChoiceField(
        choices=[(1, 'fuck'), (2, 'shit'), (3, 'cao')],
        initial=[1, 2, ],
    )

    xxoo = fields.IntegerField(
        widget=forms.SelectMultiple(choices=[(1, '欧美'), (2, '日韩'), (3, '亚洲'), ]),
        initial=[2, 3],
    )

from app01 import models
from django.forms.models import ModelChoiceField

class Love(forms.Form):
    price = fields.IntegerField()
    user_id = fields.IntegerField(
        # widget=forms.Select(choices=models.UserInfo.objects.values_list('id', 'username')),
        widget=forms.Select(),
    )
    user_id2 = ModelChoiceField(
        queryset=models.UserInfo.objects.all(),
        to_field_name='id',
    )

    def __init__(self, *args, **kwargs):
        super(__class__, self).__init__(*args, **kwargs)
        self.fields['user_id'].widget.choices = models.UserInfo.objects.values_list('id', 'username')



def love(request):
    if request.method == 'GET':
        obj = Love()
        return render(request, 'love.html', {'obj': obj, })

def test(request):
    if request.method == 'GET':
        # obj = TestForm({'city': 3})
        obj = TestForm()
        return render(request, 'test.html', {'obj': obj, })
    else:
        obj = TestForm(request.POST, request.FILES)
        if obj.is_valid():
            print("验证成功", obj.cleaned_data)  # 用户输入的信息
        else:
            print('验证失败', obj.errors)  # 验证失败的错误信息
            return render(request, 'test.html', {'obj': obj, })


class AjaxForm(forms.Form):
    username = fields.CharField()
    user_id = fields.IntegerField(
        widget=forms.Select(choices=models.UserInfo.objects.values_list('id', 'username')),
        # widget=forms.Select(),
    )
    # 单独字段的错误信息
    # 自定义方法, clean_字段名
    # 必须有返回值: self.cleaned_data['username']
    # 如果出错, raise ValidationError('用户名已存在')
    def clean_username(self):
        v = self.cleaned_data['username']
        if models.UserInfo.objects.filter(username=v).count():
            raise ValidationError('用户名已存在')
        return v

    def clean_user_id(self):
        return self.cleaned_data['user_id']

    # 整体的错误信息
    def clean(self):
        value_dict = self.cleaned_data
        v1 = value_dict.get('username')
        v2 = value_dict.get('user_id')
        if v1 == 'root' and v2 == 1:
            raise ValidationError('整体错误信息')
        return self.cleaned_data

    # 还要一个post_clean方法

import json
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

def ajax(request):
    ret = {'status': 'fuck', 'message': None}
    if request.method == 'GET':
        obj = AjaxForm()
        return render(request, 'ajax.html', {'obj': obj, })
    else:
        obj = AjaxForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            ret['status'] = '艹'
            return HttpResponse(json.dumps(ret))
        else:
            print(obj.errors)
            ret['message'] = obj.errors
            return HttpResponse(json.dumps(ret))














