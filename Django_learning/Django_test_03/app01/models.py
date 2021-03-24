from django.db import models

# Create your models here.

class UserGroup(models.Model):
    """部门"""
    title = models.CharField(max_length=32)


class UserInfo(models.Model):
    """员工"""
    # 默认的就会生成自增列，可以不写
    nid = models.AutoField(primary_key=True)  # 自增字段，int类型，设为主键
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

    # age = models.IntegerField(null=True)
    age = models.IntegerField(default=1)

    # ug_id
    ug = models.ForeignKey("UserGroup", null=True, on_delete=models.DO_NOTHING)
