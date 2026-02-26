from django.db import models

# Create your models here.
class contactDb(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Subject=models.CharField(max_length=200)
    Message=models.TextField()


class cartdb(models.Model):
    username=models.CharField(max_length=100)
    productname=models.CharField(max_length=100)
    productimage=models.ImageField(upload_to='cart_images', height_field=None,null=True,blank=True)
    price=models.IntegerField(max_length=100)
    quantity=models.CharField(max_length=100)
    total_price=models.IntegerField(max_length=100)