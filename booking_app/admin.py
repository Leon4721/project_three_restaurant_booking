from django.contrib import admin
from .models import Table, MenuItem, Booking


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'table', 'guests', 'booking_code')
    list_filter = ('date', 'table')
    search_fields = ('name', 'email', 'booking_code')
