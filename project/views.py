from django.shortcuts import render
from django.views.generic import ListView
from .models import Courses
from .tables import CoursesTable

class CoursesListView(ListView):
    model = Courses
    table_class = CoursesTable
    template_name = 'poll/courses.html'