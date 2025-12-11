from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cancel/', views.cancel, name='cancel'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('manage/', views.manage_booking, name='manage_booking'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cancel/', views.cancel, name='cancel'),
    path('manage/', views.manage_booking, name='manage_booking'),
    path('edit/<str:booking_code>/', views.edit_booking, name='edit_booking'),
    path('detail/<str:booking_code>/', views.booking_detail, name='booking_detail'),
    path('confirmed/<str:code>/', views.booking_confirmation, name='booking_confirmation'),
    path('', include('booking_app.urls')),
    path('', views.home, name='home'),
    path('manage/', views.manage_booking, name='manage_booking'),
    path('cancel/', views.cancel_booking, name='cancel_booking'),
    path('confirmed/<uuid:code>/', views.booking_confirmation, name='booking_confirmation')
]