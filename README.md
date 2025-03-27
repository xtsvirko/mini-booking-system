# 🏢 Mini Booking System

A simple Django-based application for managing facility bookings. Users can view available facilities, make bookings, and receive confirmation notifications.

---

## 🚀 Features

- User login and authenticated booking flow
- Facility capacity enforcement
- Prevention of duplicate bookings
- Only future bookings allowed (starting from tomorrow)
- Email notification simulated via Celery task
- AJAX-based booking form for better user experience
- Paginated lists for both facilities and bookings

---

## 🛠 Tech Stack

- **Python 3.12+**
- **Django**
- **Celery**
- **Redis** (used as the Celery broker)
- **Bootstrap** (for styling)

---

## 🐳 Run with Docker

1. **Create a .env file**
2. **Build and run containers**
    ```bash
    docker-compose up --build
    ```
3. **Create a superuser**
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```
##  🌐 Access the app
   Web app: http://localhost:8000