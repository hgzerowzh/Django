from django.contrib import admin

# Register your models here.

from repository import models

admin.site.register(models.UserInfo)
admin.site.register(models.UserFans)
admin.site.register(models.Blog)
admin.site.register(models.Category)
admin.site.register(models.ArticleDetail)
admin.site.register(models.Tag)
admin.site.register(models.Article)
admin.site.register(models.Article2Tag)
