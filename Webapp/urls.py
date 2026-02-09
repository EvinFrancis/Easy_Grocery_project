from django.urls import path
from Webapp import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('about/',views.about,name='about'),
]