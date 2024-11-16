from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)  # The title of the course
    description = models.TextField()  # A description of the course
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the creation date

    def __str__(self):
        return self.title
