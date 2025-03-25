from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic

from booking_system.forms import BookingForm
from booking_system.models import Facility, Booking
from booking_system.tasks import send_booking_email


# Create your views here.
class FacilityListView(generic.ListView):
    model = Facility
    paginate_by = 5
    template_name = "booking_system/facility_list.html"


class BookingListView(LoginRequiredMixin, generic.ListView):
    model = Booking
    template_name = "booking_system/booking_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).select_related("facility")


class BookingCreateView(LoginRequiredMixin, generic.CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "booking_system/booking_form.html"
    success_url = reverse_lazy("booking_system:booking_list")

    def get_initial(self):
        initial = super().get_initial()
        facility_id = self.request.GET.get("facility_id")
        if facility_id:
            initial["facility"] = facility_id
        return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["initial"]["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()
        send_booking_email.delay(self.request.user.id, self.object.id)

        return JsonResponse(
            {
                "success": True,
                "message": "Booking created! Confirmation email sent.",
            }
        )

    def form_invalid(self, form):
        error_list = []
        for field, errors in form.errors.items():
            for error in errors:
                error_list.append(str(error))

        return JsonResponse(
            {
                "success": False,
                "error": error_list[0] if error_list else "An unknown error occurred.",
            },
            status=400,
        )
