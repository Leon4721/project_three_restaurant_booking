from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MenuItem, Booking
from .forms import BookingForm, CancelBookingForm
from .forms import EditBookingForm


# -----------------------
# HOME - CREATE BOOKING + SHOW MENU
# -----------------------
def home(request):
    # Always load menu items for the right-hand card
    menu_items = MenuItem.objects.all().order_by("name")
    has_menu_items = menu_items.exists()

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            # Check for double booking of the SAME table at the SAME time
            date = form.cleaned_data["date"]
            time = form.cleaned_data["time"]
            table = form.cleaned_data["table"]

            if Booking.objects.filter(date=date, time=time, table=table).exists():
                messages.error(
                    request,
                    "That table is already booked at that time. "
                    "Please choose a different time or table."
                )
                # Re-render page with the existing form + error message
            else:
                booking = form.save()
                return redirect("booking_confirmation", code=booking.booking_code)
    else:
        form = BookingForm()

    return render(
        request,
        "booking_app/home.html",
        {
            "form": form,
            "menu_items": menu_items,
            "has_menu_items": has_menu_items,
        },
    )

# -----------------------
# CANCEL BOOKING
# -----------------------
def cancel_booking(request):
    if request.method == "POST":
        code = request.POST.get("booking_code")
        email = request.POST.get("email")

        try:
            booking = Booking.objects.get(booking_code=code, email=email)
            booking.delete()
            messages.success(request, "Your booking has been cancelled.")
            # ✅ redirect using the URL NAME below
            return redirect('cancel_booking')
        except Booking.DoesNotExist:
            messages.error(request, "No booking found with that code and email.")

    return render(request, 'booking_app/cancel_booking.html')
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
    """User can edit their booking and stay on the editor after saving."""
    booking = get_object_or_404(Booking, booking_code=booking_code)

    if request.method == "POST":
        form = EditBookingForm(request.POST, instance=booking)

        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request,
                    "Your booking has been updated. You can edit it again below if you need to."
                )
                # Stay on the same edit page
                return redirect('edit_booking', booking_code=booking.booking_code)
            except Exception:
                messages.error(
                    request,
                    "This table is already booked at that time. Please choose another time or table."
                )
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

def staff_login(request):
    return render(request, "booking_app/login.html")