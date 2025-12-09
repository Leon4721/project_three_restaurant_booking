from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MenuItem, Booking
from .forms import BookingForm, CancelBookingForm


def home(request):
    menu_items = MenuItem.objects.all()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Booking confirmed!")
                return redirect('home')
            except Exception as e:
                messages.error(request, "This table is already booked at that time.")
    else:
        form = BookingForm()

    return render(request, 'booking_app/home.html', {
        'form': form,
        'menu_items': menu_items,
    })


def cancel(request):
    if request.method == 'POST':
        form = CancelBookingForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['booking_code']
            email = form.cleaned_data['email']

            booking = Booking.objects.filter(
                booking_code=code,
                email=email
            ).first()

            if booking:
                booking.delete()
                messages.success(request, "Booking cancelled.")
                return redirect('cancel')
            else:
                messages.error(request, "Booking not found.")
    else:
        form = CancelBookingForm()

    return render(request, 'booking_app/cancel_booking.html', {'form': form})
