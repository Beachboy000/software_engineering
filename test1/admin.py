from django.contrib import admin
from .models import Item,Test1

'''
class room_reg():
    list_display=(Item.item_name)
    #filter("id")
'''
admin.site.register(Item)
admin.site.register(Test1)
# Register your models here.
