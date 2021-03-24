from django.shortcuts import render, redirect, HttpResponse
from repository import models


def home(request, site):
    """博主个人首页"""
    blog = models.Blog.objects.filter(site=site).select_related('user').first()
    if not blog:
        return redirect('/')
    tag_list = models.Tag.objects.filter(blog=blog)
    category_list = models.Category.objects.filter(blog=blog)

    date_list = models.Article.objects.raw(
        'select nid, count(nid) as num, strftime("%Y-%m", create_time) as ctime from repository_article group by strftime("%Y-%m", create_time)'
    )

    article_list = models.Article.objects.filter(blog=blog).order_by('-nid').all()

    return render(
        request,
        'home.html',
        {
            'blog': blog,
            'tag_list': tag_list,
            'category_list': category_list,
            'date_list': date_list,
            'article_list': article_list,
        }
    )