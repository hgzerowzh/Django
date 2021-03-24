from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(
        null=True,
        db_column='user',
        max_length=32,
        db_index=True,     # 只能加速查找
        unique=True,       # 加速查找，限制列值唯一
        # primary_key=True,   # 加速查找，限制列值唯一(不能为空)

        verbose_name='用户名',
        # editable=False,
    )

    user_type_choices = [
        (0, '普通用户'),
        (1, '超级用户'),
        (2, 'VIP'),
    ]
    user_type = models.IntegerField(
        choices=user_type_choices
    )

class SomeBody(models.Model):
    caption = models.CharField(max_length=12)
    pk = models.ForeignKey(
        to="UserInfo",
        to_field="id",
        on_delete=models.CASCADE,
        related_name='fuck',
    )

class Tag(models.Model):
    title = models.CharField(max_length=16)
    m = models.ManyToManyField(  # 使用ManyToManyField只能在第三张表中创建三列数据
        to='User',  # 默认和User表的主键进行关联
        through='UserToTag',  # 把下面自定义的UserToTag当做第三张表
        through_fields=['u', 't'],
    )


# 自定义ManyToMany的第三张表
class UserToTag(models.Model):
    nid = models.AutoField(primary_key=True)
    u = models.ForeignKey(to='User', on_delete=models.CASCADE)
    t = models.ForeignKey(to='Tag', on_delete=models.CASCADE)
    ctime = models.DateField()  # 这是ManyToMany中新加的字段

    class Meta:
        unique_together = [
            ('u', 't'),     # 表示u和t联合唯一
        ]
