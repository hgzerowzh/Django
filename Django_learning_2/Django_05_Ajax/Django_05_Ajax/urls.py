"""Django_05_Ajax URL Configuration

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

from django.conf.urls import url

from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^index.html$', views.index),
    url(r'^ajax1.html$', views.ajax1),
    url(r'^ajax2.html$', views.ajax2),






    url(r'^upload.html$', views.upload),
    url(r'^upload_img.html$', views.upload_img),

]
