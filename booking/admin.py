from django.contrib import admin
from .models import Facility, Booking


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "capacity")
    search_fields = ("name", "location")
    ordering = ("name",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "facility",
        "booking_date",
        "status",
        "created_at",
    )
    list_filter = ("status", "booking_date", "facility")
    search_fields = ("user__username", "user__email", "facility__name")
    ordering = ("-created_at",)
    autocomplete_fields = ("user", "facility")
