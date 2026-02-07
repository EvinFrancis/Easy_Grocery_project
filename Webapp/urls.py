from django.urls import path
from Webapp import views
urlpatterns=[
    path('home/',views.home,name='home'),
]