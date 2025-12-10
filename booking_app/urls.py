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

    # NEW: Manage booking
    path('manage/', views.manage_booking, name='manage_booking'),
    path('manage/<uuid:booking_code>/', views.edit_booking, name='edit_booking'),
    path('booking/<uuid:booking_code>/', views.booking_detail, name='booking_detail'),

]
