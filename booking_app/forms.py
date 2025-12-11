from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "name",
            "email",
            "phone",
            "date",
            "time",
            "guests",
            "table",
            "special_requests",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
        }


class CancelBookingForm(forms.Form):
    booking_code = forms.CharField(max_length=12)
    email = forms.EmailField()


class EditBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["date", "time", "guests", "table"]

    def clean(self):
        cleaned_data = super().clean()
        table = cleaned_data.get("table")
        guests = cleaned_data.get("guests")

        if table and guests and guests > table.capacity:
            raise forms.ValidationError(
                f"This table has a maximum capacity of {table.capacity} guests."
            )

        return cleaned_data
