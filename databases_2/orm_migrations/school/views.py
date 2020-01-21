from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    students = Student.objects.prefetch_related('teacher').only('name', 'group').order_by(ordering)
    context = {
        'student_list': students,
    }
    return render(request, template, context)
