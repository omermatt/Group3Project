from django.shortcuts import render
from django.views.generic import ListView
from .models import Courses, Person
from .tables import CoursesTable


class CoursesListview(ListView):
    model = Courses
    table_class = CoursesTable
    table_name = 'project/courses.hml'



class Login(ListView):
    def get(self, request):


    def post(self, request):