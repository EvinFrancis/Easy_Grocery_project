from django.shortcuts import render
from Adminapp.models import *

# Create your views here.
def home(request):
    Category=CategoryDb.objects.all()
    return render(request,'index.html' ,{"category":Category})


def about(request):
    return render(request,'about.html')
def products(request):
    Category=CategoryDb.objects.all()
    products=ProductDb.objects.all()
    return render(request,"products.html",
                  {"category":Category,
                  "products":products}
                  )
