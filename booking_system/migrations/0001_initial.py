# Generated by Django 5.1.7 on 2025-03-22 14:24

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Facility",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("location", models.CharField(max_length=255)),
                (
                    "capacity",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
            ],
            options={
                "verbose_name": "Facility",
                "verbose_name_plural": "Facilities",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Confirmed", "Confirmed"),
                            ("Declined", "Declined"),
                            ("Canceled", "Canceled"),
                        ],
                        default="Pending",
                        max_length=63,
                    ),
                ),
                ("booking_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "facility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to="booking_system.facility",
                    ),
                ),
            ],
            options={
                "verbose_name": "Booking",
                "verbose_name_plural": "Bookings",
                "ordering": ["-created_at"],
                "constraints": [
                    models.UniqueConstraint(
                        fields=("user", "facility", "booking_date"),
                        name="unique_booking_per_user_per_day",
                    )
                ],
            },
        ),
    ]
