from django.contrib import admin

# Register your models here.

from app01 import models

admin.site.register(models.Direction)
admin.site.register(models.Classification)
admin.site.register(models.Level)
admin.site.register(models.Video)
admin.site.register(models.Img)