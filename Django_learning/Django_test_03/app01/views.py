from django.shortcuts import render, HttpResponse

# Create your views here.

from django.urls import reverse
# def index(request, xx):
def index(request):
    # user_list = [
    #     'alex', 'tom', 'tony'
    # ]
    # print("URL中的是：%s" % xx)
    # a1 = reverse('a1', args=(20204, ))
    # # a1 = reverse('n1', kwargs={'a1': 1111})
    # print(a1)
    #
    # return render(request, 'index.html', {'user_list': user_list})

    from app01 import models
    # models.UserGroup.objects.create(title="销售部")
    # models.UserInfo.objects.create(username='root', password='shit', age=18, ug_id=1)

    # 查找数据：
    group_list = models.UserGroup.objects.all() # 拿到所有数据
    # group_list 是一个QuerySet类型（列表），里面的每个对象代表一行数据

    # group_list2 = models.UserGroup.objects.filter(id=1, title='shit')
    # group_list2 = models.UserGroup.objects.filter(id=1, title='shit').first()
    # group_list2 = models.UserGroup.objects.filter(id__lt=1)  # 表示id小于等于1， __lt表示小于 ，__gt表示大于

    # 删除
    models.UserGroup.objects.filter(id=2).delete()

    # 更新
    models.UserGroup.objects.filter(id=2).update(title='公关部')



    for row in group_list:
        print(row.id, row.title)

    return HttpResponse('......shit......')


def edit(request, a1):
    print(a1)
    return HttpResponse(a1)


def login(request):
    return render(request, 'login.html')