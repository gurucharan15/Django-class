from django.shortcuts import render
from .models import Student

def home(request):

    # Querying from MySQL database ('mysql_db')
    student_objects = Student.objects.all()
    # student_objects = Student.objects.using('mysql_db').all()


    data = {
    "students": ["John", "Ram", "Krishna", "David", "Charan"],
    "marks": 90,
    "name": "Guru",
    "course": "Django",
    "duration": "12 Hours",
    "age" : 21,
    "students": student_objects,
    }
    return render(request, "home.html",data
)