from django.db import models
from django.contrib import admin
# Create your models here.
class Test1(models.Model):
        test_name = models.CharField(max_length=20)
        test_name2 = models.CharField(max_length=10)
        test_num = models.CharField(max_length=20)
        test_addr = models.CharField(max_length=100)

class Item(models.Model):
        item_name = models.CharField(max_length=30)
        item_price = models.CharField(max_length=3)
        item_store = models.ForeignKey(Test1,on_delete=models.CASCADE)

