from django.shortcuts import render, HttpResponse

# Create your views here.
from app01 import models
from django.http import JsonResponse

def imgs(request):
    if request.method == 'GET':
        return render(request, 'img.html')
    else:
        nid = request.POST.get('nid')
        url_list = models.Fuckimg.objects.filter(id__gt=nid).values('id', 'src', 'title', 'summary')
        url_list = list(url_list)
        ret = {
            'status': True,
            'data': url_list,
        }
        return JsonResponse(ret)
