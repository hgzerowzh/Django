from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=32,)
    password = models.CharField(max_length=16,)
    nick_name = models.CharField(max_length=32,)
    email = models.EmailField(max_length=32,)
    create_time = models.DateTimeField(auto_now_add=True,)
    theme = models.CharField(max_length=32,)


class Music(models.Model):
    music_name = models.CharField(max_length=32,)
    link = models.CharField(max_length=128,)

    m_id = models.OneToOneField(to=Music_Info, on_delete=models.CASCADE)


class Music_Info(models.Model):
    music_author = models.CharField(max_length=32,)


class List(models.Model):
    list_name = models.CharField(max_length=32,)

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    list_music = models.ManyToManyField(to=Music,)


