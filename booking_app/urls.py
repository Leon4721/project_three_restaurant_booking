from django.urls import path
from . import views
from booking_app.views import create_admin_once

urlpatterns = [
    path('', views.home, name='home'),

 
    path('manage/', views.manage_booking, name='manage_booking'),

   
    path('cancel/', views.cancel_booking, name='cancel_booking'),

    
    path('edit/<str:booking_code>/', views.edit_booking, name='edit_booking'),
    path('detail/<str:booking_code>/', views.booking_detail, name='booking_detail'),

    
   path('confirmed/<str:code>/', views.booking_confirmation, name='booking_confirmation'),
   path('staff-login/', views.staff_login, name='staff_login'),
   path("create-admin/", create_admin_once),

]
