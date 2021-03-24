from django.shortcuts import render, HttpResponse
from app01 import models

# Create your views here.

import json

def xuliehua(request):
    return render(request, 'xuliehua.html')

from django.core import serializers
def get_data(request):
    ret = {'status': True, 'data': None, }
    # if request.method == 'GET':
    #     user_list = models.UserInfo.objects.all()
    #     return render(request, 'get_data.html', {'user_list': user_list, })

    # if request.method == 'GET':
    #     try:
    #         user_list = models.UserInfo.objects.all()
    #         ret['data'] = serializers.serialize('json', user_list)
    #     except Exception as e:
    #         ret['status'] = False
    #     result = json.dumps(ret)
    #     return HttpResponse(result)

    if request.method == 'GET':
        try:
            user_list = models.UserInfo.objects.all().values('id', 'username')
            ret['data'] = list(user_list)
        except Exception as e:
            ret['status'] = False
        result = json.dumps(ret)
        return HttpResponse(result)