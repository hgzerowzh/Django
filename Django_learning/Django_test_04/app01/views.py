from django.shortcuts import render, HttpResponse

# Create your views here.

from app01 import models
def test(request):
    """创建数据"""
    models.UserType.objects.create(title='普通用户')
    models.UserType.objects.create(title='2B用户')
    models.UserType.objects.create(title='nb用户')
    return HttpResponse("......shit......")


from django.views import View
class Login(View):
    """
    get    查
    post   创建
    put    更新
    delete 删除
    """

    def dispatch(self, request, *args, **kwargs):
        print('before')
        obj = super(Login, self).dispatch(request, *args, **kwargs)
        print('after')
        return obj

    def get(self, request):
        """在内部首先执行的是dispatch，在dispatch中拿到这个方法后做反射"""
        # return HttpResponse('Login.get')
        return render(request, 'login.html')

    def post(self, request):
        print(request.POST.get('user'))
        return HttpResponse('Login.post')


def index(request):
    """分页"""
    from django.core.paginator import Paginator, Page, PageNotAnInteger, EmptyPage

    for i in range(300):
        name = 'hgzero' + str(i)
        models.UserInfo.objects.create(name=name, age=18, ut_id=1)

    current_page = request.GET.get('page')

    user_list = models.UserInfo.objects.all()
    paginator = Paginator(user_list, 10)
    # per_page: 每页显示条目数量
    # count: 数据总个数
    # num_pages: 总页数
    # page_range: 总页数的索引范围，如：(1,10), (1,200)
    # page: page对象

    try:
        posts = paginator.page(current_page)  # 当前显示的页数，这里表示显示第一页
    except PageNotAnInteger as e:
        posts = paginator.page(1)  # 当前显示的页数，这里表示显示第一页
    except EmptyPage as e:
        posts = paginator.page(1)
    return render(request, 'index.html', {'posts': posts})





