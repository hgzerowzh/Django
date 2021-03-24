"""Django_test_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# 导入http响应客户端时所需要的模块
from django.shortcuts import HttpResponse,render,redirect
# HttpResponse直接返回字符串
# render可以直接返回html文件


def shit_login(request):
    # request 中有用户请求相关的所有信息（对象）
    # return HttpResponse("shit!!!")

    # 自动找到模板路径下的login.html文件，读取内容并返回给用户
    # 模板路径的配置要到setting.py中去修改
    return render(request, 'login.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        # 用户POST提交时提交的数据（请求体中的内容）
        u = request.POST.get('username')
        p = request.POST.get('password')
        if u == 'root' and p == 'woshiniba':
            # 登录成功，跳转到另一个页面
            # return redirect('http://hgzerowzh.com')

            # 跳转到自己的网站主页
            return redirect('/index/')
        else:
            # 登录失败
            return render(request, 'login.html', {"msg": "用户名或密码错误！"})


def index(request):
    return render(
        request,
        'index.html',
        {
            'name': 'wzg',
            'users': ['hg', 'hgzero', 'zero'],
            'users_dict': {'first': 'shit1', 'second': 'shit2', 'thrid':'shit3'},
            'users_list_dict': [
                {'id': 1, 'name': 'hghghg', 'age': 18},
                {'id': 2, 'name': 'wzhwzhwzh', 'age': 21},
                {'id': 3, 'name': 'zerozerozero', 'age': 23},
            ]
        }
    )



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('shit_login/', shit_login),
    path('login/', login),
    path('index/', index),
]
