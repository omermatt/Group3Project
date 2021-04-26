import django_tables2 as tables
from .models import Courses


class CoursesTable(tables.Table):
    class Meta:
        model = Courses
        template_name = "django_tables2/bootstrap.html"
        fields = ("name",)