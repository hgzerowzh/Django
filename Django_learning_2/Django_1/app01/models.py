from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateField()
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)

class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

class Author(models.Model):
    name = models.CharField(max_length=32)











