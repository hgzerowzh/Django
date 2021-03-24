import json
from io import BytesIO
from django.shortcuts import render, redirect, HttpResponse
from repository import models
from ..forms.account import LoginForm, RegisterForm
from utils.check_code import create_validate_code

def check_code(request):
    """验证码"""
    stream = BytesIO()  # 将图片保存到内存中
    img, code = create_validate_code()
    img.save(stream, 'PNG')
    request.session['CheckCode'] = code
    return HttpResponse(stream.getvalue())


def login(request):
    """登录"""
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        result = {'status': False, 'message': None, 'data': None}
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user_info = models.UserInfo.objects.\
                filter(username=username, password=password). \
                values('nid', 'nickname',
                       'username', 'email',
                       'avatar',
                       'blog__nid',
                       'blog__site').first()
            if not user_info:
                result['message'] = '用户名或密码错误'
            else:
                result['status'] = True
                request.session['user_info'] = user_info
                if form.cleaned_data.get('rmb'):        # 是否勾选了30天免登陆
                    request.session.set_expiry(60*60*24*30)   # session保存30天
        else:
            print(form.errors)
            if 'check_code' in form.errors:
                result['message'] = '验证码错误或过期'
            else:
                result['message'] = '用户名或密码错误'
        return HttpResponse(json.dumps(result))

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        result = {'status': False, 'message': None, }
        register_form = RegisterForm(request=request, data=request.POST)
        if register_form.is_valid():
            r_username = register_form.cleaned_data.get('username')
            r_password = register_form.cleaned_data.get('password')
            r_email = register_form.cleaned_data.get('email')
            models.UserInfo.objects.create(
                username=r_username,
                password=r_password,
                email=r_email
            )
            result['status'] = True
        else:
            print(register_form.errors)
            if 'check_code' in register_form.errors:
                result['message'] = '验证码错误或过期'
            elif 'email' in register_form.errors:
                result['message'] = '邮箱格式错误'
            else:
                result['message'] = '不好意思，出错了!'
        return HttpResponse(json.dumps(result))

def home(request):
    return redirect('http://cnblogs.com/hgzero')


