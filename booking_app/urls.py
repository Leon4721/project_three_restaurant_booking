from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Manage existing booking
    path('manage/', views.manage_booking, name='manage_booking'),

    # Cancel booking
    path('cancel/', views.cancel_booking, name='cancel_booking'),

    # Edit booking
    path('edit/<str:booking_code>/', views.edit_booking, name='edit_booking'),

    # Booking detail
    path('detail/<str:booking_code>/', views.booking_detail, name='booking_detail'),

    # Booking confirmation
    path('confirmed/<str:code>/', views.booking_confirmation, name='booking_confirmation'),

    # Staff login
    path('staff-login/', views.staff_login, name='staff_login'),
]
