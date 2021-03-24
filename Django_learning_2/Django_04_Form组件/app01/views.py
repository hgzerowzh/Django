from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

from django import forms
from django.forms import fields
class F1Form(forms.Form):
    user = fields.CharField(
        max_length=18,
        min_length=3,
        required=True,
        error_messages={
            'required': '用户名不能为空',
            'max_length': 'sorry,太长了',
            'min_length': 'sorry,太短了',
            'invalid': '请输入字符',
        }
    )
    pwd = fields.CharField(required=True, min_length=6)
    age = fields.IntegerField(required=True, error_messages={
        'required': '年龄不能为空',
        'invalid': '请输入数字',
        }
    )
    email = fields.EmailField(required=True,)

def index(request):
    if request.method == 'GET':
        obj = F1Form()
        return render(request, 'index.html', {'obj': obj})
    else:
        obj = F1Form(request.POST)
        if obj.is_valid():
            print("验证成功", obj.cleaned_data) # 用户输入的信息
        else:
            print('验证失败', obj.errors)      # 验证失败的错误信息
            return render(request, 'index.html', {'obj': obj, })






from app01 import models
from app01.forms import UserForm

def users(request):
    user_list = models.UserInfo.objects.all()
    return render(request, 'user.html', {'user_list': user_list,})

def add_user(request):
    if request.method == 'GET':
        obj = UserForm()
        return render(request, 'add_user.html', {'obj': obj})
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)  # cleaned_data的格式: {'username': 'xxxxx', 'email': 'xxx@qq.com'}
            # models.UserInfo.objects.create(
            #     username=obj.cleaned_data['user'],
            #     email=obj.cleaned_data['email'],
            # )
            models.UserInfo.objects.create(**obj.cleaned_data)
            return redirect('/users/')

        else:
            return render(request, 'add_user.html', {'obj': obj})

def edit_user(request, nid):
    if request.method == 'GET':
        data = models.UserInfo.objects.filter(id=nid).first()
        obj = UserForm({'username': data.username, 'email': data.email})
        return render(request, 'edit_user.html', {'obj': obj, 'nid': nid, })
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            models.UserInfo.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect('/users/')
        else:
            return render(request, 'edit_user.html', {'obj': obj, 'nid': nid, })

















