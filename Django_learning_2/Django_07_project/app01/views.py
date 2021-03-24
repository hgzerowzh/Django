from django.shortcuts import render, HttpResponse
from app01 import models
import json

def video(request, *args, **kwargs):
    condition = {}  # 构造一个查询字典，这里面将保存查询条件
    for k, v in kwargs.items(): # 获取url后面的每个键值对参数的值，就是拿到每个数字
        temp = int(v)           # url中的字符类型，要转换为int类型
        kwargs[k] = temp
        if temp:
            condition[k] = temp

    # 从数据库取出所有的类型、等级、状态
    class_list = models.Classification.objects.all()
    level_list = models.Level.objects.all()
    status_list = list(map(lambda x: {'id': x[0], 'name': x[1]}, models.Video.status_choice))
    # 视频的上下线状态保存的形式：[(1, '下线'), (2, '上线'), ]，这里用map函数将其迭代改造成字典的形式

    # 直接传入包含查询条件的字典，这个字典中保存的就是url中的参数键值对
    video_list = models.Video.objects.filter(**condition)

    return render(
        request,
        'video.html',
        {
            'class_list': class_list,
            'level_list': level_list,
            'status_list': status_list,
            'kwargs': kwargs,     # 将url中的参数也传递给模板
            'video_list': video_list,
        }
    )

def video2(request, *args, **kwargs):
    condition = {}               # 构造一个查询字典
    for k, v in kwargs.items():  # 将url传过来的键值对中的数字转换为int类型
        temp = int(v)
        kwargs[k] = temp

    # 拿到url中对应各个键的值
    direction_id = kwargs.get('direction_id')
    classification_id = kwargs.get('classification_id')
    level_id = kwargs.get('level_id')
    level_list = models.Level.objects.all()

    # 从数据库中拿到所有的方向，因为方向会一直在页面上显示
    direction_list = models.Direction.objects.all()

    # 方向若选了0，也就是全部，则会显示所有的技术类型
    if direction_id == 0:
        class_list = models.Classification.objects.all()
        # 进入技术类型判断的逻辑
        #   如果是0显示全部，本来上上一层逻辑中就是显示全部技术类型，则可以忽略，
        #   如果显示指定的技术类型，则在condition中写入一个查询键值对
        if classification_id == 0:
            pass
        else:
            condition['classification_id'] = classification_id
    # 若用户选择了某个方向(非0)，则进入以下逻辑
    else:
        direction_obj = models.Direction.objects.filter(id=direction_id).first()
        class_list = direction_obj.classification.all()

        # 拿到指定某个方向下的所有技术类型的id，以键值对的形式返回
        vlist = direction_obj.classification.all().values_list('id')

        # 构造一个包含某个方向下的所有技术类型id值的列表，若该方向下无技术类型，则该技术类型列表留空
        if not vlist:
            classification_id_list = []
        else:
            classification_id_list = list(zip(*vlist))[0]

        # 若技术类型选择了0(全部)，则构造一个包含in关键字的查询条件，查找所有符合条件的技术类型
        if classification_id == 0:
            condition['classification_id__in'] = classification_id_list
        # 若选择了某技术类型，且当前选中的技术类型在某方向的技术类型列表中，则查询条件为查找指定技术类型
        # 否则进入查询全部技术类型的逻辑(也就是选中了某个技术类型，而下一次选择的方向中不包含这个技术类型，)
        else:
            if classification_id in classification_id_list:
                condition['classification_id'] = classification_id
            else:
                # 例如: 指定方向[1,2,3] , 而分类为5时, 就走这里的条件
                kwargs['classification_id'] = 0
                condition['classification_id__in'] = classification_id_list

    # 等级的筛选，选中全部则忽略，否则就加一个查询条件
    if level_id == 0:
        pass
    else:
        condition['level_id'] = level_id

    # 传入构造好的查询字典，到数据库进行筛选，得到包含全部符合条件video的列表
    video_list = models.Video.objects.filter(**condition)

    return render(
        request,
        'video2.html',
        {
            'direction_list': direction_list, # 方向列表
            'class_list': class_list,         # 类型列表
            'level_list': level_list,         # 等级列表
            'video_list': video_list,         # 视频列表
            'kwargs': kwargs,                 # 包含当前url传入参数的列表
        }
    )

from django.http import JsonResponse
def imgs(request):
    if request.method == 'GET':
        return render(request, 'img.html')
    elif request.method == 'POST':
        nid = request.POST.get('nid')
        img_list = models.Img.objects.filter(id__gt=nid).values('id', 'src', 'title')
        img_list = list(img_list)
        ret = {
            'status': True,
            'data': img_list,
        }
        # return HttpResponse(json.dumps(ret))  # 这样也行
        return JsonResponse(ret)


