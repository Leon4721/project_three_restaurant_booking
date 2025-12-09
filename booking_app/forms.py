from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date', 'time', 'guests', 'table']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }


class CancelBookingForm(forms.Form):
    booking_code = forms.UUIDField()
    email = forms.EmailField()
