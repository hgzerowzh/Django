from django.db import models

# Create your models here.


class Classes(models.Model):
    """班级表"""
    title = models.CharField(max_length=32)
    m = models.ManyToManyField("Teachers")
    # m = models.ManyToManyField("Teachers", related_name='teacher_xxx')


class Teachers(models.Model):
    """老师表"""
    name = models.CharField(max_length=32)

# class C2T(models.Model):
#     cid = models.ForeignKey(Classes)
#     tid = models.ForeignKey(Teachers)

class Student(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    cs = models.ForeignKey(Classes, on_delete=models.CASCADE)
    # cs = models.ForeignKey(Classes, related_name='class_xxx', on_delete=models.CASCADE)
