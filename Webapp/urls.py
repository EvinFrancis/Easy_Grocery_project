from django.urls import path
from Webapp import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('about/',views.about,name='about'),
    path('filtered_products/<cat_name>/',views.filtered_products,name='filtered_products'),
    path("single_vegetable/<int:prod_id>/",views.single_vegetable,name='single_vegetable'),
    path('contact/',views.contact,name='contact'),
    
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('save_user/',views.save_user,name='save_user'),
    path('user_log_in/',views.user_log_in,name='user_log_in'),
    path('user_log_out/',views.user_log_out,name='user_log_out'),
    path('cart/',views.cart,name='cart'),
    
    
]