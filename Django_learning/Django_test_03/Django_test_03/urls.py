"""Django_test_03 URL Configuration

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

from django.conf.urls import url, include
from app01 import views

from django.shortcuts import HttpResponse

# urlpatterns = [
#     path('admin/', admin.site.urls),
#
# ]

def default(request):
    return HttpResponse('出错了！')


urlpatterns = [
    # url(r'^index/(\d+)/', views.index, name='a1'),
    url(r'^index/', views.index, name='a1'),


    # url(r'^edit/(?P<a1>\w+)/(?P<a2>\w+)', views.edit),
    url(r'^edit/(\w+).html$', views.edit),
    url(r'^edit/(\w+)/', views.edit, name='n2'),

    url(r'^login/', views.login, name='m1'),






    url(r'^app01/', include('app01.urls')),
    url(r'^app02/', include('app02.urls')),

    url(r'^', default),
]
