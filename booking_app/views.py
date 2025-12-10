from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MenuItem, Booking
from .forms import BookingForm, CancelBookingForm
from .forms import EditBookingForm



# -----------------------
# HOME - CREATE BOOKING
# -----------------------
def home(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():

            # Check for double booking
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']

            if Booking.objects.filter(date=date, time=time).exists():
                messages.error(request, "That time slot is already booked. Please pick another.")
                return redirect('home')

            booking = form.save()
            return redirect('booking_confirmation', code=booking.booking_code)

    else:
        form = BookingForm()

    return render(request, 'booking_app/home.html', {'form': form})


# -----------------------
# CANCEL BOOKING
# -----------------------
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


# -----------------------
# MANAGE BOOKING (step 1)
# -----------------------
def manage_booking(request):
    """User enters booking code + email to load their booking."""
    booking = None

    if request.method == "POST":
        code = request.POST.get("booking_code")
        email = request.POST.get("email")

        booking = Booking.objects.filter(
            booking_code=code,
            email=email
        ).first()

        if booking:
            return redirect('edit_booking', booking_code=booking.booking_code)
        else:
            messages.error(request, "Booking not found. Check your code and email.")

    return render(request, "booking_app/manage_booking.html")


# -----------------------
# EDIT BOOKING
# -----------------------
def edit_booking(request, booking_code):
    booking = Booking.objects.filter(booking_code=booking_code).first()

    if not booking:
        messages.error(request, "Booking not found.")
        return redirect('manage_booking')

    if request.method == "POST":
        form = EditBookingForm(request.POST, instance=booking)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Your booking has been updated successfully.")
                return redirect('booking_detail', booking_code=booking.booking_code)
            except Exception:
                messages.error(request, "This table is already booked at that time.")
    else:
        form = EditBookingForm(instance=booking)

    return render(request, "booking_app/edit_booking.html", {
        "booking": booking,
        "form": form
    })


# -----------------------
# BOOKING DETAIL (after edit)
# -----------------------
def booking_detail(request, booking_code):
    booking = Booking.objects.filter(booking_code=booking_code).first()

    if not booking:
        messages.error(request, "Booking not found.")
        return redirect('manage_booking')

    return render(request, "booking_app/booking_detail.html", {
        "booking": booking
    })


# -----------------------
# CONFIRMATION PAGE
# -----------------------
def booking_confirmation(request, code):
    booking = Booking.objects.get(booking_code=code)
    return render(request, 'booking_app/confirmation.html', {'booking': booking})
