from django import forms

from .models import Booking


class BookingForm(forms.ModelForm):
    booking_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="Select booking date",
    )

    class Meta:
        model = Booking
        fields = ["facility", "booking_date"]
        widgets = {
            "facility": forms.Select(attrs={"class": "form-control"}),
        }
