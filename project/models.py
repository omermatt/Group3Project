from django.db import models


# Create your models here.
# the courses for the application
class Courses(models.Model):
    name = models.CharField(max_length=5000, verbose_name="Course name")


class Person(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50, blank=True)

