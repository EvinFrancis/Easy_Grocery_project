from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    CategoryName=models.CharField( max_length=50,unique=True)
    Description=models.TextField()
    CategoryImage=models.ImageField(upload_to="categories")
    # def __str__(self):
    #     return self.CategoryName # 
class ProductDb(models.Model):
    ProductName=models.CharField(max_length=100)
    Description=models.TextField()
    Price=models.DecimalField(max_digits=10,decimal_places=2)
    ProductImage=models.ImageField(upload_to="products")
    
    Category=models.CharField(max_length=50)
    def __str__(self):
        return self.ProductName
class serviceDb(models.Model):
    ServiceName=models.CharField(max_length=100)
    Description=models.TextField()
    ServiceImage=models.ImageField(upload_to="services")
    def __str__(self):
        return self.ServiceName

class Registrationdb(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)    
    password=models.CharField(max_length=100)
    confrimpassword=models.CharField(max_length=100)
    def __str__(self):
        return self.username