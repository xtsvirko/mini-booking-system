from django import forms
from django.core.exceptions import ValidationError
from datetime import date, timedelta

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

    def clean(self):
        cleaned_data = super().clean()
        user = self.initial.get("user") or self.instance.user
        facility = cleaned_data.get("facility")
        booking_date = cleaned_data.get("booking_date")

        if facility and booking_date and user:

            tomorrow = date.today() + timedelta(days=1)
            if booking_date < tomorrow:
                raise ValidationError("You can only book starting from tomorrow.")

            existing_bookings = Booking.objects.filter(
                facility=facility,
                booking_date=booking_date,
            ).count()

            if existing_bookings >= facility.capacity:
                raise ValidationError(
                    f"No more available slots for {facility.name} on {booking_date}."
                )

            if Booking.objects.filter(
                user=user,
                facility=facility,
                booking_date=booking_date,
            ).exists():
                raise ValidationError(
                    f"You have already booked {facility.name} on {booking_date}."
                )

        return cleaned_data
