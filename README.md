# mini-booking-system
![img.png](img.png)

📌 Django Take-Home Assignment: “Mini Booking System”

📝 Project Brief

Build a small Django application for a simple booking system where users can book available slots

for a facility.

🎯 Key Features:

1. User Registration & Authentication (Django’s built-in auth system)

2. Facility Model (e.g., name, location, capacity)

3. Booking Model (e.g., user, facility, date, status)

4. Django Forms for Booking Creation

5. Class-Based Views (CBVs) for Booking Management

6. Basic Templates for Facility & Booking Listings

7. Admin Panel Customization (optional but good for extra points)

8. Unit Tests for critical functionality

9. Database Optimization Considerations (indexes, constraints, efficient queries)

10. Dockerized Application (see details below)

🚀 Docker Requirements

•

•

•

•

The project should be fully containerized with a Dockerfile and docker-compose.yml.

The application should run with:

•

Django backend in one container.

•

PostgreSQL database in another container.

A simple README.md should include setup instructions (e.g., docker-compose up).

Bonus if it includes environment variable management (.env file).

💡 Assessment Criteria:•

•

•

•

•

•

Code Quality & Readability – Clean, modular, and maintainable code.

Django Best Practices – Proper use of models, views, forms, and templates.

Design Decisions – Scalable data models and well-structured views.

Testing & Error Handling – Coverage for edge cases and robust form validation.

Extensibility & Maintainability – How easily can features be added or modified?

Docker Implementation – Proper separation of concerns, working Dockerfile, and

docker-compose.

⏳ Time & Expectations

•

•

Time Estimate: ~1 week

Submission: GitHub repo with a README explaining setup, design choices, and areas for

improvement.

🔥 Bonus Ideas (Optional, Extra Points)

•

•

•

•

•

AJAX for Asynchronous Booking (e.g., avoid page reloads when submitting forms).

Celery for Background Tasks (e.g., sending booking confirmation emails).

Custom User Model for Future Scalability.

CSS Styling with Bootstrap/Tailwind for a better UI.

Health Check Endpoint for Docker container monitoring.