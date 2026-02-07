from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login
from Adminapp.models import CategoryDb,ProductDb

# Create your views here.
def admin_dashboard(request):
    return render(request, 'dashboard.html')
def admin_loginpage(request):
    return render(request, 'admin_login.html')

def admin_login(request):
    if request.method =='POST':
        uname=request.POST.get('username')
        pswd=request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pswd)
            if user is not None:
                login(request,user)
                request.session['username']=uname
                request.session['password']=pswd
                return redirect(admin_dashboard)
            else:
                print("Password incorrect;;;;")
                return redirect(admin_loginpage)
            
        else:
             print("Username not found;;;;")
             return redirect(admin_loginpage)

def admin_logout(request):  
    del request.session['username']
    del request.session['password']
    return redirect(admin_loginpage)


def add_products(request):
    category=CategoryDb.objects.all()
    return render (request,'add_products.html',{"categories": category})
def add_category(request):
    if request.method=="POST":
        category=request.POST.get("category_name")
        Des=request.POST.get("description")
        imga=request.FILES.get("category_image")
        obj=CategoryDb(CategoryName=category,Description=Des,CategoryImage=imga)
        obj.save()
        
    return render (request,'add_categories.html')

def category(request):
    if request.method=="POST":
        category=request.POST.get("category_name")
        Des=request.POST.get("description")
        imga=request.FILES.get("category_image")
        obj=CategoryDb(CategoryName=category,Description=Des,CategoryImage=imga)
        obj.save()
        return  redirect("add_category")

def view_products(request):
    products=ProductDb.objects.all()#fetch all the data from the ProductDb table and store it in the variable products.

    return render (request,'view_products.html',{"products": products})#products is the name of the variable used in the html file to access the data.

def display_categories(request):
    category=CategoryDb.objects.all()
    return render(request,"view_categories.html",{"categories": category})

def delete_category(request,cat_id):
    category=CategoryDb.objects.get(id=cat_id)
    category.delete()
    return redirect(display_categories)
def edit_category(request,cat_id):
    if request.method=="POST":
        category_name=request.POST.get("category_name")
        description=request.POST.get("description")
        if request.FILES.get("category_image"): 
            image=request.FILES.get("category_image") #If user uploads a new image → update it.
                 
                 #If not → keep the old image.”
        else:
            image=CategoryDb.objects.get(id=cat_id).CategoryImage
         
        obj=CategoryDb.objects.filter(id=cat_id).update(CategoryName=category_name,Description=description,CategoryImage=image)
        return redirect(display_categories)
    

def edit_categorypage(request,cat_id):
    category=CategoryDb.objects.get(id=cat_id)
    return render(request,"edit_category.html",{"category":category})

#save produacts//
def save_product(request):
    if request.method=="POST":
        produact_name=request.POST.get("product_name")
        description=request.POST.get("description")
        price=request.POST.get("price")
        
        product_image=request.FILES.get("product_image")   
        
        Category_Name=request.POST.get("category")  
        obj1=ProductDb(ProductName=produact_name,Description=description,Price=price,Category=Category_Name,ProductImage=product_image)
        obj1.save()  
        return redirect(add_products)
    
    #delete products//

def delete_product(request,prod_id):
    products=ProductDb.objects.get(id=prod_id)
    products.delete()
    return redirect(view_products)

#edit products//
def edit_productpage(request,prod_id):
    obj=ProductDb.objects.get(id=prod_id)
    return render(request,"edit_products.html",{"product":obj})


#update products//
def edit_product(request,prod_id):
    if request.method=="POST":
        product_name=request.POST.get("product_name")
        description=request.POST.get("description")
        price=request.POST.get("price")
        if request.FILES.get("product_image"): 
            product_image=request.FILES.get("product_image") #If user uploads a new image → update it.
                 
                 #If not → keep the old image.”
        else:
            product_image=ProductDb.objects.get(id=prod_id).ProductImage
        category_name=request.POST.get("category")
        obj=ProductDb.objects.filter(id=prod_id).update(ProductName=product_name,Description=description,Price=price,Category=category_name,ProductImage=product_image)
        return redirect(view_products)



