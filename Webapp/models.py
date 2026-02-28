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

class chechoutdb(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100,null=True,blank=True)
    pin=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    totalprice=models.IntegerField(max_length=100)

  