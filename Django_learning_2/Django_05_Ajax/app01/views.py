from django.shortcuts import render, HttpResponse

# Create your views here.

from django import forms
from django.forms import fields
class UploadForm(forms.Form):
    user = fields.CharField()
    img = fields.FileField()

import json

def upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html')
    else:
        # obj = UploadForm(request.POST, request.FILES)
        # if obj.is_valid():
        #     user = obj.cleaned_data['user']
        #     img = obj.cleaned_data['img']

        user = request.POST.get('user')
        img = request.FILES.get('img')
        # # img是对象(文件大小, 文件名称, 文件内容)
        # # print(img.name)
        # # print(img.size)

        f = open(img.name, 'wb')
        for line in img.chunks():
            f.write(line)
        f.close()
        return HttpResponse('shitshitshit!')

def upload_img(request):
    import os
    import uuid
    nid = str(uuid.uuid4())
    ret = {'status': True, 'data': None, 'message': None, }
    obj = request.FILES.get('k3')
    file_path = os.path.join('static', nid+obj.name)
    f = open(file_path, 'wb')
    for line in obj.chunks():
        f.write(line)
    f.close()
    ret['data'] = file_path
    return HttpResponse(json.dumps(ret))



# Ajax全套
def index(request):
    return render(request, 'index.html')

def ajax1(request):
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    ret = {'status': True, 'message': '...'}
    import json
    return HttpResponse(json.dumps(ret))

def ajax2(request):
    pass