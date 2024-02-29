from django.db import models
from django.contrib import admin
class BooK(models.Model):
   bookno=models.IntegerField(primary_key=True);
   bookname=models.CharField(max_length=20);
   bookprice=models.IntegerField(help_text="Enter the price of book");
   quantity=models.IntegerField();
   authorname=models.CharField(max_length=50);
class BookAdmin(admin.ModelAdmin):
   list_display=("bookno","bookname","bookprice","quantity","authorname");