from django.urls import path
from Webapp import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('about/',views.about,name='about'),
    path('filtered_products/<cat_name>/',views.filtered_products,name='filtered_products'),
    path("single_vegetable/<prod_name>/",views.single_vegetable,name='single_vegetable'),
]