import django_tables2 as tables
from .models import Courses

class CoursesTable(tables.Table):
    class Meta:
        model =Courses
        table_name = "django_tables2/boostrap.html"
        fields = (" Course name",)