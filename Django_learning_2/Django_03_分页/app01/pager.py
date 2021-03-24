class Paginator(object):
    def __init__(self, totalCount, currentPage, perPageItemNum=10, maxPageNum=11):
        """
        totalCount：数据总个数
        currentPage：当前页
        perPageItemNum: 每页显示的行数
        maxPageNum：最多显示的页码个数
        """
        self.total_count = totalCount
        try:
            v = int(currentPage)
            if v <= 0:
                v = 1
            self.current_page = v
        except Exception as e:
            self.current_page = 1
        self.per_page_item_num = perPageItemNum
        self.max_page_num = maxPageNum

    @property
    def start(self):
        """数据切片的起始位置"""
        return (self.current_page-1) * self.per_page_item_num

    @property
    def end(self):
        """数据切片的结束位置"""
        return self.current_page * self.per_page_item_num

    @property
    def num_pages(self):
        """总的页数"""
        a, b = divmod(self.total_count, self.per_page_item_num)
        if b == 0:
            return a
        return a + 1

    def page_num_range(self):
        """页码范围"""
        part = int(self.max_page_num / 2)
        # 总的页数少于默认要显示的页码数
        if self.num_pages < self.max_page_num:
            return range(1, self.num_pages + 1)
        # 当前页码处于第一页的前一半位置
        if self.current_page - part < 1:
            return range(1, self.max_page_num + 1)
        # 当前页码处于最后一页的后一半位置
        if self.current_page + part > self.num_pages:
            return range(self.num_pages - self.max_page_num + 1, self.num_pages + 1)
        return range(self.current_page - part, self.current_page + part + 1)

    def page_str(self):
        """生成所有的页码"""
        # 创建一个保存所有页码的容器
        page_list = []

        # 生成首页和上一页的页码
        first = "<li><a href='?p=1'>首页</a></li>"
        page_list.append(first)
        if self.current_page == 1:
            the_prev = "<li><a href='#'>上一页</a></li>"
        else:
            the_prev = "<li><a href='?p=%s'>上一页</a></li>" % (self.current_page - 1, )
        page_list.append(the_prev)

        # 生成中间所有页的页码
        for i in self.page_num_range():
            if i == self.current_page:
                temp = "<li class='active'><a href='?p=%s'>%s</a></li>" % (i, i, )
            else:
                temp = "<li><a href='?p=%s'>%s</a></li>" % (i, i, )
            page_list.append(temp)

        # 生成下一页和尾页的页码
        if self.current_page == self.num_pages:
            the_next = "<li><a href='#'>下一页</a></li>"
        else:
            the_next = "<li><a href='?p=%s'>下一页</a></li>" % (self.current_page + 1, )
        page_list.append(the_next)
        last = "<li><a href='?p=%s'>尾页</a></li>" % (self.num_pages, )
        page_list.append(last)

        # 列表容器中的各个页码转换为字符串
        result = ''.join(page_list)
        return result

