"""
URL configuration for programing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Define the home view
def home(request):
    return HttpResponse("Hello, World! Welcome to the Programming Platform!")

# Combine all URL routes into one urlpatterns list
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('', home, name='home'),  # Home route
    path('courses/', include('courses.urls')),  # Include the courses app URLs
]
