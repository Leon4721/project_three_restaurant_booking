from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cancel/', views.cancel, name='cancel'),

    path('manage/', views.manage_booking, name='manage_booking'),
    path('edit/<str:booking_code>/', views.edit_booking, name='edit_booking'),
    path('detail/<str:booking_code>/', views.booking_detail, name='booking_detail'),

    path('confirmed/<str:code>/', views.booking_confirmation, name='booking_confirmation'),
]
