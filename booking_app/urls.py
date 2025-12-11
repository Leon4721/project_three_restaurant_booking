from django.urls import path
from . import views
from booking_app.views import create_admin_once

urlpatterns = [
    path('', views.home, name='home'),

    # Manage existing booking
    path('manage/', views.manage_booking, name='manage_booking'),

    # Cancel booking
    # 🔹 IMPORTANT: make sure your view is called cancel_booking in views.py
    path('cancel/', views.cancel_booking, name='cancel_booking'),

    # Optional extra views if you have them
    path('edit/<str:booking_code>/', views.edit_booking, name='edit_booking'),
    path('detail/<str:booking_code>/', views.booking_detail, name='booking_detail'),

    # Booking confirmation page
    # If your booking_code is a UUIDField, uuid is fine here
   path('confirmed/<str:code>/', views.booking_confirmation, name='booking_confirmation'),
   path('staff-login/', views.staff_login, name='staff_login'),
   path("create-admin/", create_admin_once),

]
