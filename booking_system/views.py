from django.urls import reverse_lazy
from django.views import generic

from booking_system.forms import BookingForm
from booking_system.models import Facility, Booking


# Create your views here.
class FacilityListView(generic.ListView):
    model = Facility
    paginate_by = 5
    template_name = "booking_system/facility_list.html"


class BookingListView(generic.ListView):
    model = Booking
    template_name = "booking_system/booking_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).select_related("facility")


class BookingCreateView(generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking_system/booking_form.html"
    success_url = reverse_lazy("booking_system:facility_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
