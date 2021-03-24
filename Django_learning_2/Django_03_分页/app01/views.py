from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

user_list = []
for i in range(1, 200):
    temp = {'username': 'root' + str(i), 'age': i, }
    user_list.append(temp)


def index(request):
    page_num = int(request.GET.get('p'))

    per_page_count = 10
    start_page = per_page_count*(page_num-1)
    end_page = per_page_count*page_num
    data = user_list[start_page:end_page]

    prev_page = page_num-1
    next_page = page_num+1

    if page_num <= 1:
        prev_page = 1

    return render(request, 'index.html', {'user_list': data, 'prev_page': prev_page, 'next_page': next_page, })


class CustomPaginator(Paginator):
    def __init__(self, current_page, max_page_num, *args, **kwargs):
        self.current_page = int(current_page)
        self.max_page_num = max_page_num
        super(CustomPaginator, self).__init__(*args, **kwargs)

    def page_num_range(self):
        part = int(self.max_page_num / 2)
        if self.num_pages < self.max_page_num:
            return range(1, self.max_page_num + 1)
        if self.current_page - part < 1:
            return range(1, self.max_page_num + 1)
        if self.current_page + part > self.num_pages:
            return range(self.num_pages - self.max_page_num + 1, self.num_pages + 1)
        return range(self.current_page - part, self.current_page + part + 1)


def index1(request):
    current_page = request.GET.get('p')
    paginator = CustomPaginator(current_page, 11, user_list, 10)
    try:
        posts = paginator.page(current_page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request, 'index1.html', {'posts': posts, })


def index2(request):
    # 获取当前页码号
    current_page = int(request.GET.get('p'))
    # 导入自定义分页插件
    from app01.pager import Paginator
    # 参数依次为: 数据总个数, 当前页码号, 每页显示的行数, 最多显示的页码个数
    # 后两个参数默认为: 10, 11
    obj = Paginator(200, current_page,)
    # obj对象中可调用的属性(方法):
    #     start       当前页的起始条目索引
    #     end         当前页的结束条目索引
    #     page_str()  生成的所有页码结构和样式
    data_list = user_list[obj.start:obj.end]
    return render(request, 'index2.html', {'data': data_list, 'page_obj': obj, })












