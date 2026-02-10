from django.shortcuts import render
from Adminapp.models import *

# Create your views here.
def home(request):
    Category=CategoryDb.objects.all()
    latest_products=ProductDb.objects.order_by('-id')[:4]#fetch the latest 4 products from the ProductDb table and store it in the variable latest_products.
    return render(request,'index.html' ,{"category":Category
                                         ,"latest_products":latest_products})


def about(request):
    return render(request,'about.html')
def products(request):
    Category=CategoryDb.objects.all()
    products=ProductDb.objects.all()
    first_pro=ProductDb.objects.order_by('id')[:3]#fetch the first product from the ProductDb table and store it in the variable first_product.
    our_products=ProductDb.objects.order_by('id')[0:8]#fetch the products from the ProductDb table starting from the 4th product and store it in the variable our_products.
    latest_pro=ProductDb.objects.order_by('-id')[:3]#fetch the latest 3 products from the ProductDb table and store it in the variable latest_products.
    return render(request,"products.html",
                  {"category":Category,
                  "products":products,
                  "latest_pro":latest_pro,
                    "first_pro":first_pro,
                    "our_products":our_products
                   }
                  )

def filtered_products(request ,cat_name):
    products_filtered=ProductDb.objects.filter(Category=cat_name)
    
    return render(request,'filtered_products.html',{"products":products_filtered
                        
                                                    })
