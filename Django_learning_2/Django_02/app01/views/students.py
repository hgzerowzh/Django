from django.shortcuts import render, redirect, HttpResponse
from app01 import models

import json



def get_students(request):
    stu_list = models.Student.objects.all()
    cls_list = models.Classes.objects.all()
    return render(request, 'get_students.html', {'stu_list': stu_list, 'cls_list': cls_list, })

def add_students(request):
    if request.method == "GET":
        class_list = models.Classes.objects.all()
        return render(request, 'add_students.html', {'class_list': class_list})
    elif request.method == "POST":
        stu_name = request.POST.get('stu_name')
        stu_age = request.POST.get('stu_age')
        stu_gender = int(request.POST.get('stu_gender'))
        stu_class_id = request.POST.get('stu_class_id')
        models.Student.objects.create(username=stu_name, age=stu_age, gender=stu_gender, cs_id=stu_class_id)
        return redirect('/students.html')

def del_students(request):
    stu_id = request.GET.get('nid')
    models.Student.objects.filter(id=stu_id).delete()
    return redirect('/students.html')

def edit_students(request):
    if request.method == "GET":
        stu_id = request.GET.get('nid')
        stu_obj = models.Student.objects.filter(id=stu_id).first()
        class_list = models.Classes.objects.values('id', 'title')
        return render(request, 'edit_students.html', {'stu_obj': stu_obj, 'class_obj': class_list})
    elif request.method == "POST":
        stu_id = request.GET.get('nid')
        stu_name = request.POST.get('stu_name')
        stu_age = request.POST.get('stu_age')
        stu_gender = request.POST.get('stu_gender')
        stu_class_id = request.POST.get('stu_class_id')
        models.Student.objects.filter(id=stu_id).update(username=stu_name, age=stu_age, gender=stu_gender, cs_id=stu_class_id)
        return redirect('/students.html')

# Ajax的方式实现学生的增删改查

def ajax_add_students(request):
    if request.method == "POST":
        ret_message = {'message': None, 'flag': True, 'stu_id': None}
        try:
            u = request.POST.get('username')
            a = request.POST.get('age')
            g = request.POST.get('gender')
            c = request.POST.get('the_class')
            stu_obj = models.Student.objects.create(
                username=u,
                age=a,
                gender=g,
                cs_id=c,
            )
            ret_message['stu_id'] = stu_obj.id
        except Exception as e:
            ret_message['flag'] = False
            ret_message['message'] = "用户输入错误!"
        return HttpResponse(json.dumps(ret_message))

def ajax_del_students(request):
    if request.method == "POST":
        data = {'flag': True, 'message': None}
        try:
            stu_id = request.POST.get('stu_id')
            models.Student.objects.filter(id=stu_id).delete()
        except Exception as e:
            data['flag'] = False
            data['message'] = '不好意思，出错了！'
        return HttpResponse(json.dumps(data))

def ajax_edit_students(request):
    if request.method == "POST":
        data = {'flag': True, 'message': None}
        try:
            stu_id = request.POST.get('stu_id')
            stu_name = request.POST.get('stu_name')
            stu_age = request.POST.get('stu_age')
            stu_gender = request.POST.get('gender')
            stu_class = request.POST.get('stu_class')

            models.Student.objects.filter(id=stu_id).update(
                username=stu_name,
                age=stu_age,
                gender=stu_gender,
                cs_id=stu_class,
            )
        except Exception as e:
            data['flag'] = False
            data['message'] = "更新失败!"
        return HttpResponse(json.dumps(data))




