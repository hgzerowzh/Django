from django.shortcuts import render, redirect, HttpResponse

from app01 import models

def get_classes(request):
    cls_list = models.Classes.objects.all()
    return render(request, 'get_classes.html', {"cls_list": cls_list})

def add_classes(request):
    if request.method == "GET":
        return render(request, 'add_classes.html')
    elif request.method == "POST":
        # 获取表单中输入的课程名后，添加到数据库中
        the_title = request.POST.get('title')
        models.Classes.objects.create(title=the_title)
        return redirect('/classes.html')

def del_classes(request):
    nid = request.GET.get('nid')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('/classes.html')

def edit_classes(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        obj = models.Classes.objects.filter(id=nid).first()
        return render(request, 'edit_classes.html', {'obj': obj})
    elif request.method == "POST":
        nid = request.GET.get('nid')
        the_title = request.POST.get('title')
        models.Classes.objects.filter(id=nid).update(title=the_title)
        return redirect('/classes.html')

def set_teachers(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        class_obj = models.Classes.objects.filter(id=nid).first() # 拿到相应课程号的课程对象
        class_teacher_list = class_obj.m.all()                    # 拿到该课程对象相关的所有老师对象
        all_teacher_list = models.Teachers.objects.all()          # 拿到所有的老师对象

        class_teacher_num_list = []
        for i in class_teacher_list:
            class_teacher_num_list.append(i.id)

        return render(
            request,
            'set_teachers.html',
            {
                'class_teacher_list': class_teacher_num_list,
                'all_teacher_list': all_teacher_list,
                'nid': nid,
            }
        )
    elif request.method == "POST":
        nid = request.GET.get('nid')
        teachers = request.POST.getlist('set_teachers')
        class_id = models.Classes.objects.filter(id=nid).first()
        class_id.m.set(teachers)
        return redirect('/classes.html')







