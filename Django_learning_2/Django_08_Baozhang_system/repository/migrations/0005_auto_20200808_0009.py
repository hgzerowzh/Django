# Generated by Django 3.0.8 on 2020-08-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_auto_20200807_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
    ]
