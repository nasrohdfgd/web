from django.shortcuts import render
from .models import Course

def course_list(request):
    courses = Course.objects.all()  # Retrieve all courses from the database
    return render(request, 'courses/course_list.html', {'courses': courses})
