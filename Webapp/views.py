from django.shortcuts import render,redirect
from Adminapp.models import *
from Webapp.models import *

# Create your views here.
def home(request):
    serv=serviceDb.objects.all()#fetch all the data from the serviceDb table and store it in the variable serv.
    Category=CategoryDb.objects.all()
    latest_products=ProductDb.objects.order_by('-id')[:4]#fetch the latest 4 products from the ProductDb table and store it in the variable latest_products.
    return render(request,'index.html' ,{"category":Category
                                         ,"latest_products":latest_products
                                         ,"services":serv
                                         })


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


def single_vegetable(request,prod_id):
    pro_name=ProductDb.objects.get(id=prod_id)
    return render(request,'single_vegetable.html',{"product":pro_name})

def contact(request):
    contacts=contactDb.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        obj=contactDb(Name=name,Email=email,Subject=subject,Message=message)
        obj.save()
    return render(request,'contact.html')

def signin(request):
    return render(request,'signin_page.html')


def signup(request):
    return render(request,"signUp.html")

#save user sing up
def save_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        
        obj=Registrationdb(username=username,email=email,password=password,confrimpassword=confirm_password)
        if Registrationdb.objects.filter(email=email).exists():
            print("email already exists")
            return redirect(signup)
        elif Registrationdb.objects.filter(username=username).exists():
            print("username already exists")
            return redirect(signup)
        else:
            obj.save()
            return redirect(signup)
    
#user login
def user_log_in(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if Registrationdb.objects.filter(username=username,password=password).exists():
            #sesssion creations
            request.session['username']=username
            request.session['password']=password
            return redirect(home)
        else:
            return redirect(signin)
        #session creations and redirection to home page after successful login.
        
def user_log_out(request):
    del request.session['username']
    del request.session['password']
    return redirect(home)  #session deletion and redirection to home page after logout. 
           


# view car page

def cart(request):
    return render(request,'cart.html')