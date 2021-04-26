from django.db import models


# Create your models here.
# the courses for the application
class Courses(models.Model):
    name = models.CharField(max_length=5000, verbose_name="Course name")
