from django.conf.urls import url
from .views import account
from .views import home

urlpatterns = [
    url(r'^register.html$', account.register),
    url(r'^login.html$', account.login),

    url(r'^check_code.html$', account.check_code),

    url(r'^home$', account.home),

    url(r'^(?P<site>\w+).html$', home.home),


]