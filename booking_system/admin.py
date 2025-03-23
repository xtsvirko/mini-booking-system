from django.contrib import admin
from .models import Facility, Booking


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0
    readonly_fields = ("user", "booking_date", "status", "created_at")
    can_delete = False
    show_change_link = True


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "capacity")
    search_fields = ("name", "location")
    ordering = ("name",)
    inlines = [BookingInline]


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
