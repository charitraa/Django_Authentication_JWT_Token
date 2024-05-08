from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200,default='')
    phone = models.IntegerField()
    address = models.CharField(max_length=200,default='')
    email = models.EmailField(max_length=200,default='')
    password = models.CharField(max_length=200,default='')
