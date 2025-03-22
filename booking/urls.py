from django.contrib import admin
from django.urls import path

from booking.views import FacilityListView

app_name = "booking"
urlpatterns = [
    path("facilities/", FacilityListView.as_view(), name="facility_list"),
]
