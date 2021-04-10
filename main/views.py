from django.shortcuts import render

from main.models import Teacher


def index(request):
    teacher = Teacher.objects.all()
    return render(request, 'main/index.html', {"teachers": teacher})
