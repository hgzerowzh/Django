# Generated by Django 3.0.8 on 2020-08-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fuckimg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(max_length=256, verbose_name='图片URL')),
                ('title', models.CharField(max_length=32, verbose_name='图片标题')),
                ('summary', models.CharField(max_length=128, verbose_name='摘要信息')),
            ],
        ),
    ]
