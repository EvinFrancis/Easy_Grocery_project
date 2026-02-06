from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    CategoryName=models.CharField( max_length=50,unique=True)
    Description=models.TextField()
    CategoryImage=models.ImageField(upload_to="categories")
    def __str__(self):
        return self.CategoryName # 
