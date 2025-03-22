from django.contrib import admin
from django.urls import path


app_name = "booking"
urlpatterns = [
    path("", admin.site.urls),
]
