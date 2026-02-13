from django.urls import path
from Adminapp import views


urlpatterns = [
    path('dashboard/',views.admin_dashboard,name='admin_dashboard'), 
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_loginpage/',views.admin_loginpage,name='admin_loginpage'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('add_products/',views.add_products,name='add_products'), 
    path('add_category/',views.add_category,name='add_category'),
    path('view_products/',views.view_products,name='view_products'),
    path('category',views.category,name='category'),
    path('display_categories/', views.display_categories, name='display_categories'),
    path('delete_category/<int:cat_id>/', views.delete_category, name='delete_category'),
    path('edit_category/<int:cat_id>/', views.edit_category, name='edit_category'),
    path('edit_categorypage/<int:cat_id>/', views.edit_categorypage, name='edit_categorypage'),
    path('save_product/',views.save_product,name='save_product'),
    path('view_products/',views.view_products,name='view_products'),
    path('delete_product/<int:prod_id>/',views.delete_product,name='delete_product'),
    path('edit_productpage/<int:prod_id>/',views.edit_productpage,name='edit_productpage'),
    path('edit_product/<int:prod_id>/',views.edit_product,name='edit_product'),
    path('add_service/',views.add_service,name='add_service'),
    path('save_service/',views.save_service,name='save_service'),
    path('view_services/',views.view_services,name='view_services'),
    path('contact_info/',views.contact_info,name='contact_info'),
    



    

]
