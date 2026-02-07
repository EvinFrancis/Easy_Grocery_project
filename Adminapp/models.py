from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    CategoryName=models.CharField( max_length=50,unique=True)
    Description=models.TextField()
    CategoryImage=models.ImageField(upload_to="categories")
    def __str__(self):
        return self.CategoryName # 
class ProductDb(models.Model):
    ProductName=models.CharField(max_length=100)
    Description=models.TextField()
    Price=models.DecimalField(max_digits=10,decimal_places=2)
    ProductImage=models.ImageField(upload_to="products")
    
    Category=models.CharField(max_length=50)
    def __str__(self):
        return self.ProductName
