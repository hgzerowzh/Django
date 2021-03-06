"""Django_02 URL Configuration

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

from app01.views import classes, students

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^classes.html', classes.get_classes),
    url(r'^add_classes.html', classes.add_classes),
    url(r'^del_classes.html', classes.del_classes),
    url(r'^edit_classes.html', classes.edit_classes),

    url(r'^set_teachers.html', classes.set_teachers),


    url(r'^students.html', students.get_students),
    url(r'^add_students.html', students.add_students),
    url(r'^del_students.html', students.del_students),
    url(r'^edit_students.html', students.edit_students),

    url(r'^ajax_add_students.html', students.ajax_add_students),
    url(r'^ajax_del_students.html', students.ajax_del_students),
    url(r'^ajax_edit_students.html', students.ajax_edit_students),

]
