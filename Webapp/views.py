from django.shortcuts import render,redirect
from Adminapp.models import *
from Webapp.models import *
from django.contrib import messages
from decimal import Decimal
import razorpay



# Create your views here.
def home(request):
    serv=serviceDb.objects.all()#fetch all the data from the serviceDb table and store it in the variable serv.
    Category=CategoryDb.objects.all()
    cart=0
    latest_products=ProductDb.objects.order_by('-id')[:4]#fetch the latest 4 products from the ProductDb table and store it in the variable latest_products.
    uname = request.session.get('username')
    if uname:
    
            cart=cartdb.objects.filter(username=uname).count()

    return render(request,'index.html' ,{"category":Category
                                         ,"latest_products":latest_products
                                         ,"services":serv,'cart':cart
                                         })


def about(request):
    cart=0

    uname = request.session.get('username')
    if uname:
    
            cart=cartdb.objects.filter(username=uname).count()
    serv=serviceDb.objects.all()#fetch all the data from the serviceDb table and store it in the variable serv.

    return render(request,'about.html',{"services":serv,'cart':cart})
def products(request):
    cart=0

    serv=serviceDb.objects.all()#fetch all the data from the serviceDb table and store it in the variable serv.
    uname = request.session.get('username')
    if uname:
    
            cart=cartdb.objects.filter(username=uname).count()
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
                    "our_products":our_products,
                    "services":serv,"cart":cart
                   }
                  )

def filtered_products(request ,cat_name):
    cart=0
    uname = request.session.get('username')
    if uname:
    
            cart=cartdb.objects.filter(username=uname).count()
    products_filtered=ProductDb.objects.filter(Category=cat_name)
    
    
    return render(request,'filtered_products.html',{"products":products_filtered,'cart':cart
                        
                                                    })


def single_vegetable(request,prod_id):
    cart=0
    uname = request.session.get('username')
    if uname:
    
            cart=cartdb.objects.filter(username=uname).count()
    pro_name=ProductDb.objects.get(id=prod_id)
    return render(request,'single_vegetable.html',{"product":pro_name,'cart':cart})

def contact(request):
    cart=0
    contacts=contactDb.objects.all()
    uname = request.session.get('username')
    if uname:
    
            cart=cartdb.objects.filter(username=uname).count()
    
    

    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        obj=contactDb(Name=name,Email=email,Subject=subject,Message=message)
        obj.save()
    return render(request,'contact_page.html')

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
            messages.warning(request,"email already exists")
            return redirect(signup)
        elif Registrationdb.objects.filter(username=username).exists():
            messages.warning(request,"Username already exists")
            print("username already exists")
            return redirect(signup)
        elif Registrationdb.objects.filter(password=confirm_password).exists():
            messages.warning(request,"Password doesn't match")
            print("Password doesn't match")
            return redirect(signup)
        else:
            obj.save()
            messages.success(request,"Registration successfully")
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
            messages.success(request,"Login successfully")
            return redirect(home)
        else:
            messages.warning(request,"Invalid username or password")
            return redirect(signin)
        #session creations and redirection to home page after successful login.
        
def user_log_out(request):
    del request.session['username']
    del request.session['password']
    return redirect(home)  #session deletion and redirection to home page after logout. 
           


# view cart page

def cart(request):
    username = request.session.get('username')

    if not username:
       return redirect(signin)
    cart=0
    uname = request.session.get('username')
    if uname:
    
            cart=cartdb.objects.filter(username=uname).count()
    usname=request.session['username']
    data=cartdb.objects.filter(username=usname)
    sub_total=0
    delivery=0
    grand_total=0
    user_data=cartdb.objects.filter(username=usname)
    for i in user_data:
    
        sub_total +=i.total_price
        if sub_total>1000:
            delivery=0
        elif sub_total>500:
            delivery=50
        else:
            delivery=100
        grand_total=sub_total+delivery
    return render(request,'cart.html',{"data":data
                                       ,"sub_total":sub_total
                                       ,"delivery":delivery
                                       ,"grand_total":grand_total,"cart":cart
                                       })



def cart_save(request):
    if request.method=="POST":
        username=request.POST.get("username")
        name=request.POST.get("pname")
        quantity=request.POST.get("quantity")
        price=Decimal(request.POST.get("price"))
        total=Decimal(request.POST.get("total"))
        pro=ProductDb.objects.filter(ProductName=name).first()
        product_img=pro.ProductImage if pro else None
        obj=cartdb(productname=name,quantity=quantity,price=price,username=username,total_price=total,productimage=product_img)
        obj.save()
    return redirect(cart)

def delete_cart(request,cart_id):
    
    cartdb.objects.filter(id=cart_id).delete()
    messages.error(request,"Product deleted successfully")
    return redirect(cart)

def checkout_page(request): 
    username = request.session.get('username')

    if not username:
       return redirect(signin)
    cart=0
    uname = request.session.get('username')
    if uname:
         cart=cartdb.objects.filter(username=uname).count()
    usname=request.session['username']
    sub_total=0
    delivery=0
    grand_total=0

    user_data=cartdb.objects.filter(username=usname)
    for i in user_data:
    
        sub_total +=i.total_price
        if sub_total>1000:
            delivery=0
        elif sub_total>500:
            delivery=50
        else:
            delivery=100
        grand_total=sub_total+delivery
    return render(request,'check_out_page.html',{"data":user_data
                                       ,"sub_total":sub_total
                                       ,"delivery":delivery
                                       ,"grand_total":grand_total,'cart':cart
                                       })

#savwe checkout page
def checkout_save(request):
     if request.method=="POST":
        firstname=request.POST.get("first_name")
        lastname=request.POST.get("last_name") 
        country=request.POST.get("country")
        address=request.POST.get("address")
        city=request.POST.get("city")
        state=request.POST.get("state")
        pincode=request.POST.get("pincode")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        totalprice=request.POST.get("grand_total")
        obj=chechoutdb(firstname=firstname,lastname=lastname,country=country,address=address,city=city,state=state,pin=pincode,email=email,mobile=phone,totalprice=totalprice)
        obj.save()
        return redirect(paytment_page)
     


def paytment_page(request):
    categories=CategoryDb.objects.all()
    uname = request.session.get('username')
    cart_total=0
    if uname:
    
            cart_total=cartdb.objects.filter(username=uname).count()
    customer=chechoutdb.objects.order_by('-id').first()
    payy=customer.totalprice
    amount=int(payy*100)
    payy_str=str(amount)
    
    if request.method=="POST":
         order_currency="INR"
         client=razorpay.Client(auth=("rzp_test_0ib0jPwwZ7I1lT", "VjHNO5zKeKxz8PYe7VnzwxMR"))
         payment=client.order.create({'amount':amount,'currency':order_currency})
         
    
    return render(request,'payment_page.html',{
         'category':categories,"cart_total":cart_total,
         "payy_str":payy_str
    })


