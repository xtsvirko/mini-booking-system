# Generated by Django 5.1.7 on 2025-03-26 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking_system", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="booking_date",
            field=models.DateField(db_index=True),
        ),
        migrations.AlterField(
            model_name="booking",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Confirmed", "Confirmed"),
                    ("Declined", "Declined"),
                    ("Canceled", "Canceled"),
                ],
                db_index=True,
                default="Pending",
                max_length=63,
            ),
        ),
    ]
