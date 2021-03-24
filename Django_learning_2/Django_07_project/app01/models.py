from django.db import models

# Create your models here.

class Direction(models.Model):
    """方向：自动化，测试，运维，前端"""
    # weight = models.IntegerField(verbose_name="权重(按从大到小排列)", default=0)
    name = models.CharField(verbose_name='名称', max_length=32)
    classification = models.ManyToManyField('Classification')

    class Meta:
        db_table = 'Direction'                  # 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
        verbose_name_plural = '方向(视频方向)'  # 设置admin中的表名

    def __str__(self):
        return self.name


class Classification(models.Model):
    """分类：Python，Linux，JavaScript，OpenStack，Node.js"""
    # weight = models.IntegerField(verbose_name='权重(按从大到小排列)', default=0)
    name = models.CharField(verbose_name='名称', max_length=32)

    class Meta:
        db_table = 'Classification'
        verbose_name_plural = '分类(视频分类)'

    def __str__(self):
        return self.name


class Level(models.Model):
    title = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = '难度级别'

    def __str__(self):
        return self.title


class Video(models.Model):
    status_choice = (    # 视频的上下线状态
        (1, '下线'),
        (2, '上线'),
    )
    # level_choice = (
    #     (1, '初级'),
    #     (2, '中级'),
    #     (3, '高级'),
    # )
    status = models.IntegerField(verbose_name='状态', choices=status_choice, default=1) # 视频上下线状态，默认是1, 也就是下线状态
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    # level = models.IntegerField(verbose_name='级别', choices=level_choice, default=1)
    classification = models.ForeignKey('Classification', null=True, blank=True, on_delete=models.CASCADE)

    weight = models.IntegerField(verbose_name='权重(按从大到小排列)', default=0)

    title = models.CharField(verbose_name='标题', max_length=32)
    summary = models.CharField(verbose_name='简介', max_length=32)
    # img = models.ImageField(verbose_name='图片', upload_to='./static/images/Video/')
    img = models.CharField(verbose_name='图片', max_length=32)
    href = models.CharField(verbose_name='视频地址', max_length=256)

    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Video'
        verbose_name_plural = '视频'

    def __str__(self):
        return self.title


class Img(models.Model):
    # src = models.CharField(max_length=32, verbose_name='图片路径')
    src = models.FileField(max_length=32, verbose_name='图片路径', upload_to='static/upload')
    title = models.CharField(max_length=16, verbose_name='标题')
    summary = models.CharField(max_length=128, verbose_name='简介')

    class Meta:
        verbose_name_plural = '图片'

    def __str__(self):    # 在admin中显示每个img对象对应的title，否则每个对象都会显示Img object
        return self.title















