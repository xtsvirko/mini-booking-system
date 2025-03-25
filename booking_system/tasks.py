import time
from celery import shared_task


@shared_task
def send_booking_email(user_id, booking_id):
    time.sleep(1)
    print(f"✅ Email sent to user ID {user_id} about booking ID {booking_id}")
