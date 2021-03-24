from django.urls import path

from django.conf.urls import url
from app01 import views

from django.shortcuts import HttpResponse



# urlpatterns = [
#     path('admin/', admin.site.urls),
#
# ]

urlpatterns = [
    url(r'^index.html/', views.index),

]
