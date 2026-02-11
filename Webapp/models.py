from django.db import models

# Create your models here.
class contactDb(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Subject=models.CharField(max_length=200)
    Message=models.TextField()