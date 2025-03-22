from django.shortcuts import render
from django.views import generic

from booking.models import Facility


# Create your views here.
class FacilityListView(generic.ListView):
    model = Facility
    paginate_by = 5
    template_name = "booking/facility_list.html"
