from django.urls import path

from booking_system.views import FacilityListView, BookingCreateView, BookingListView

app_name = "booking_system"

urlpatterns = [
    path("", FacilityListView.as_view(), name="facility_list"),
    path("facilities/", FacilityListView.as_view(), name="facility_list"),
    path("bookings/", BookingListView.as_view(), name="booking_list"),
    path("bookings/create/", BookingCreateView.as_view(), name="booking_create"),
]
