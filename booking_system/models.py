from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Facility(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = _("Facility")
        verbose_name_plural = _("Facilities")


class Booking(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "Pending", _("Pending")
        CONFIRMED = "Confirmed", _("Confirmed")
        DECLINED = "Declined", _("Declined")
        CANCELED = "Canceled", _("Canceled")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="bookings",
        on_delete=models.CASCADE,
    )
    facility = models.ForeignKey(
        Facility, on_delete=models.CASCADE, related_name="bookings"
    )
    status = models.CharField(
        max_length=63,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
        db_index=True,
    )
    booking_date = models.DateField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.facility.name} ({self.booking_date})"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "facility", "booking_date"],
                name="unique_booking_per_user_per_day",
            )
        ]
